from contextlib import asynccontextmanager
import logging

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from motor.motor_asyncio import AsyncIOMotorClient
from crud import router as crud_router
import os

MONGO_URL = os.getenv("MONGODB_URI",
                      "mongodb+srv://wings:P1gG3F4ZJLcJvld0@cluster0.vzgllba.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
logging.info(f"Connecting to MongoDB: {MONGO_URL}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = AsyncIOMotorClient(MONGO_URL)
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

    port = int(os.getenv("PORT", 8001))
    uvicorn.run(app, host="127.0.0.1", port=port)
