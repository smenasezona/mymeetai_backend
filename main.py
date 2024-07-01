from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from datetime import date
from typing import Optional

app = FastAPI()

MONGO_URL = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URL)
db = client.bookstore
collection = db.books


class Book(BaseModel):
    title: str
    author: str
    genre: str
    release_date: date
    cover: Optional[str] = None


@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(MONGO_URL)
    app.mongodb = app.mongodb_client.bookstore


@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client = AsyncIOMotorClient(MONGO_URL)
    app.mongodb_client.close()


__all__ = ["Book", "collection"]
