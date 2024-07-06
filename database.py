from motor.motor_asyncio import AsyncIOMotorClient

from main import MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)

db = client.bookstore
collection = db.books
