import os
import sys
import django

# === Setup Django Environment ===
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library

print("\n=== Django ORM Relationship Queries ===\n")

# 1️⃣ Query all books by a specific author
try:
    author = Author.objects.get(name="J.K. Rowling")
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}: {[book.title for book in books_by_author]}")
except Author.DoesNotExist:
    print("❌ Author 'J.K. Rowling' not found. Please add this author in the admin panel or shell.")

# 2️⃣ List all books in a library
try:
    library = Library.objects.get(name="Central Library")
    books_in_library = library.books.all()
    print(f"Books in {library.name}: {[book.title for book in books_in_library]}")
except Library.DoesNotExist:
    print("❌ Library 'Central Library' not found. Please create it in the admin panel or shell.")

# 3️⃣ Retrieve the librarian for a library
try:
    library = Library.objects.get(name="Central Library")
    if hasattr(library, "librarian"):
        print(f"Librarian of {library.name}: {library.librarian.name}")
    else:
        print(f"⚠️ No librarian assigned to '{library.name}'.")
except Library.DoesNotExist:
    print("❌ Cannot retrieve librarian — library not found.")
