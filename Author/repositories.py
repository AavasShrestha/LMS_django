from .models import Author

class AuthorRepository:
    def create_author(self, author_data):
        return Author.objects.create(**author_data)

    def get_author_by_id(self, authorid):
        try:
            return Author.objects.get(authorid=authorid, is_deleted=False)
        except Author.DoesNotExist:
            return None

    def get_all_authors(self):
        return Author.objects.filter(is_deleted=False)

def update_book(self, bookid, updated_data):
    book = self.get_book(bookid)  # Fetch the book instance
    
    for key, value in updated_data.items():
        if key == "authorid":  # Ensure foreign key is assigned correctly
            try:
                value = Author.objects.get(id=value)  # Fetch the author instance
            except Author.DoesNotExist:
                raise ValueError(f"Author with ID {value} does not exist")
        setattr(book, key, value)
    
    book.save()
    return book

    def delete_author(self, authorid):
        author = self.get_author_by_id(authorid)
        if not author:
            return None

        author.is_deleted = True  # Soft delete
        author.save()
        return author
