from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'The Quantum Realm', 'author': 'Alice Newton', 'category': 'science'},
    {'title': 'Journey to the Stars', 'author': 'Brian Carter', 'category': 'science'},
    {'title': 'Mysteries of the Mind', 'author': 'Clara Hughes', 'category': 'psychology'},
    {'title': 'The Art of Code', 'author': 'David Kim', 'category': 'technology'},
    {'title': 'Whispers of History', 'author': 'Ella Martinez', 'category': 'history'},
    {'title': 'Poetry of the Soul', 'author': 'Farhan Ali', 'category': 'literature'},
    {'title': 'Economics Simplified', 'author': 'Grace Thompson', 'category': 'economics'}
]

@app.get("/books")
async def get_all_books():
    """
    This is an operation that provides list of all books.
    No input required.
    It returns a list of books.
    """
    return BOOKS

@app.get("/books/mybook")
async def get_all_books():
    return {"mybook" : "mybook"}

@app.get("/books/{boot_title}")
async def get_all_books(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def get_books_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.get('title').casefold():
            BOOKS[i].update(update_book)

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS[i].pop('title')
            break


#===============================