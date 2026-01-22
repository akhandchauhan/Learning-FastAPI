from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

def load_data():
    with open("books.json", "r") as f:
        data = json.load(f)
        return data


@app.get('/')
def welcome():
    return {"message": "Hey there, Welcome to my Library API"}


@app.get('/about')
def info():
    return {
        "message": "This api purpose is to give info about books with their author, title and rating"
    }


@app.get('/books')
def book_info():
    data = load_data()
    return data


@app.get('/book/{book_id}')
def specific_book_info(
    book_id: str = Path(..., description="ID of the book", example="B001")
):
    data = load_data()

    if book_id in data:
        return data[book_id]
    else:
        raise HTTPException(
            status_code=404,
            detail="Book not found in books json"
        )


@app.get('/filter')
def filtered_info(
    min_rating: float = Query(0, description="Minimum rating"),
    max_pages: int = Query(999999999, description="Maximum pages")
):
    data = load_data()
    filtered_books = {}

    for book_id, book_details in data.items():
        if (
            book_details.get("rating", 0) >= min_rating
            and book_details.get("pages", 0) <= max_pages
        ):
            filtered_books[book_id] = book_details

    return filtered_books


    