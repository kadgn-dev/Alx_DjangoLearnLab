import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "J.K. Rowling"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")
except Author.DoesNotExist:
    print(f"Author '{author_name}' not found.")

# List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library.name}: {[book.title for book in books_in_library]}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")

# Retrieve the librarian for a library
try:
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian for {library.name}: {librarian.name}")
except (Library.DoesNotExist, Librarian.DoesNotExist):
    print(f"No librarian found for '{library_name}'.")
