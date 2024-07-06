from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from motor.motor_asyncio import AsyncIOMotorClient
from crud import router as crud_router

MONGO_URL = "mongodb+srv://wings:<password>@cluster0.vzgllba.mongodb.net/"
client = AsyncIOMotorClient(MONGO_URL)
db = client.bookstore
collection = db.books


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = AsyncIOMotorClient(MONGO_URL)
    app.mongodb = app.mongodb_client.bookstore
    yield
    app.mongodb_client.close()


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(crud_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8001)
