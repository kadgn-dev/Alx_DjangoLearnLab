# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve the book by title
book = Book.objects.get(title="1984")
book
# Expected Output: <Book: 1984 by George Orwell (1949)>

# Retrieve all books
Book.objects.all()
# Expected Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>
