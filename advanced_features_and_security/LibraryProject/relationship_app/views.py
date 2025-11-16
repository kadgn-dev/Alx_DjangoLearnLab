from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .models import Library, Book, UserProfile, Author
from .forms import BookSearchForm   # <-- Secure form imported


# --------------------------------------------------
# Secure Book List View (ALX Requirement)
# --------------------------------------------------
@login_required
@permission_required('relationship_app.can_view', raise_exception=True)
def list_books(request):
    """
    SECURE VERSION:
    - Uses Django ORM (prevents SQL injection)
    - Validates input using Django forms
    - Works with CSRF-protected POST search form
    """
    books = Book.objects.all()
    form = BookSearchForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        query = form.cleaned_data.get("query")
        if query:
            # ORM FILTER protects against SQL injection
            books = books.filter(title__icontains=query)

    return render(request, "relationship_app/list_books.html", {
        "books": books,
        "form": form
    })


# --------------------------------------------------
# Library Detail View
# --------------------------------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# --------------------------------------------------
# User Registration View
# --------------------------------------------------
def register(request):
    """
    Secure registration:
    - Uses Django's UserCreationForm (validated input)
    - Protected by CSRF token automatically
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# --------------------------------------------------
# Role-Based Access Control
# --------------------------------------------------
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# --------------------------------------------------
# Permission-Protected Book Management Views
# --------------------------------------------------

# Create Book — secure with ORM & validation
@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    """
    Secure Add Book:
    - Uses ORM only
    - Validates POST data
    - Prevents improper input by checking for valid author ID
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')

        if title and author_id:
            author = get_object_or_404(Author, id=author_id)
            Book.objects.create(title=title.strip(), author=author)
            return redirect('list_books')

    authors = Author.objects.all()
    return render(request, 'relationship_app/add_book.html', {'authors': authors})


# Edit Book — secure editing
@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    """
    Secure Edit Book:
    - Uses ORM updates
    - Validates fields before saving
    - Uses get_object_or_404 for safe access
    """
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')

        if title:
            book.title = title.strip()

        if author_id:
            book.author = get_object_or_404(Author, id=author_id)

        book.save()
        return redirect('list_books')

    authors = Author.objects.all()
    return render(request, 'relationship_app/edit_book.html', {'book': book, 'authors': authors})


# Delete Book — secured with POST + ORM
@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    """
    Secure Delete:
    - Data deletion only allowed via POST (prevents CSRF vulnerabilities)
    - ORM ensures safe deletion
    """
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('list_books')

    return render(request, 'relationship_app/delete_book.html', {'book': book})
