from pydantic import BaseModel, Field
from fastapi import FastAPI, Body
from pydantic_core.core_schema import BoolSchema

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

BOOKS = [
    Book(1, "The Quantum Realm", "Alice Newton", "science", 5),
    Book(2, "Journey to the Stars", "Brian Carter", "science", 1),
    Book(3, "Mysteries of the Mind", "Clara Hughes", "science", 4),
    Book(4, "The Art of Code", "three", "science", 3),
    Book(5, "Whispers of History", "four", "science", 2)
]

@app.get("/books")
async def get_all_books():
    """
    This is an operation that provides list of all books.
    No input required.
    It returns a list of books.
    """
    return BOOKS

@app.post("/create-book")
async def create_book(create_book=Body()):
    BOOKS.append(create_book)