from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book


# ============================================
# View Books (Required by ALX: function name MUST be book_list)
# ============================================
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


# ============================================
# Add Book (Requires can_create)
# ============================================
@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        year = request.POST.get("year")

        if title and author and year:
            Book.objects.create(
                title=title,
                author=author,
                publication_year=year
            )
            return redirect('book_list')

    return render(request, 'bookshelf/add_book.html')


# ============================================
# Edit Book (Requires can_edit)
# ============================================
@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):

    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.publication_year = request.POST.get("year")
        book.save()
        return redirect('book_list')

    return render(request, 'bookshelf/edit_book.html', {'book': book})


# ============================================
# Delete Book (Requires can_delete)
# ============================================
@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):

    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()
        return redirect('book_list')

    return render(request, 'bookshelf/delete_book.html', {'book': book})
