from fastapi import HTTPException, FastAPI
from bson import ObjectId

from main import Book, collection

app = FastAPI()


@app.post("/books/", response_model=Book)
async def create_book(book: Book):
    new_book = await collection.insert_one(book.dict())
    created_book = await collection.find_one({"_id": new_book.inserted_id})
    return created_book


@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: str):
    book = await collection.find_one({"_id": ObjectId(book_id)})
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.get("/books/", response_model=list[Book])
async def read_books():
    books = await collection.find().to_list(1000)
    return books


@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: str, book: Book):
    updated_book = await collection.find_one_and_update(
        {"_id": ObjectId(book_id)},
        {"$set": book.dict()},
        return_document=True
    )
    if updated_book:
        return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}")
async def delete_book(book_id: str):
    delete_result = await collection.delete_one({"_id": ObjectId(book_id)})
    if delete_result.deleted_count == 1:
        return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
