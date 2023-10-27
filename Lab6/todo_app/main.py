from fastapi import FastAPI, Query, Path

app = FastAPI()

# GET ReST API
@app.get("/books/")
def get_books(category: str = Query(None)):
    return {"message": f"GET books with category: {category}"}

# GET ReST API with path parameters
@app.get("/books/{book_id}")
def get_book(book_id: int = Path(..., description="The ID of the book")):
    return {"message": f"GET book with ID: {book_id}"}

# GET ReST API with query parameters and path parameters
@app.get("/authors/{author_id}")
def get_author(
    author_id: int = Path(..., description="The ID of the author"),
    books: str = Query(None),
):
    return {"message": f"GET author with ID: {author_id} and books: {books}"}

# POST ReST API
@app.post("/books/")
def create_book(book: dict):
    return {"message": "POST book", "data": book}

# PUT ReST API
@app.put("/books/{book_id}")
def update_book(book_id: int, book: dict):
    return {"message": f"PUT book with ID: {book_id}", "data": book}

# DELETE ReST API
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    return {"message": f"DELETE book with ID: {book_id}"}
