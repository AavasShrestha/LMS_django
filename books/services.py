from .repositories import BookRepository

class BookService:
    def __init__(self):
        self.repo = BookRepository()

    def add_book(self, book_data):
        return self.repo.create_book(book_data)

    def get_book_detail(self, bookid):
        book = self.repo.get_book_by_id(bookid)
        if not book:
            return {"error": "Book not found"}
        return book

    def get_all_books(self):
        return self.repo.get_all_books()

    def update_book(self, bookid, updated_data):
        book = self.repo.get_book_by_id(bookid)
        if not book:
            return {"error": "Book not found"}

        updated_book = self.repo.update_book(bookid, updated_data)
        return updated_book

    def delete_book(self, bookid):
        book = self.repo.get_book_by_id(bookid)
        if not book:
            return {"error": "Book not found"}

        self.repo.delete_book(bookid)
        return {"message": "Book deleted successfully"}
