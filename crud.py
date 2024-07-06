from fastapi import HTTPException, APIRouter
from bson import ObjectId
from models import Book
from database import collection

router = APIRouter()


@router.post("/books/", response_model=Book)
async def create_book(book: Book):
    new_book = await collection.insert_one(book.dict(by_alias=True))
    created_book = await collection.find_one({"_id": new_book.inserted_id})
    return created_book


@router.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: str):
    book = await collection.find_one({"_id": ObjectId(book_id)})
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")


@router.get("/books/", response_model=list[Book])
async def read_books(skip: int = 0, limit: int = 10):
    books = await collection.find().skip(skip).limit(limit).to_list(limit)
    return books


@router.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: str, book: Book):
    updated_book = await collection.find_one_and_update(
        {"_id": ObjectId(book_id)},
        {"$set": book.dict(by_alias=True)},
        return_document=True
    )
    if updated_book:
        return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


@router.delete("/books/{book_id}")
async def delete_book(book_id: str):
    delete_result = await collection.delete_one({"_id": ObjectId(book_id)})
    if delete_result.deleted_count == 1:
        return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
