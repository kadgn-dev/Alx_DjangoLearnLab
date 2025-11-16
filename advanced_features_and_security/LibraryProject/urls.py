from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('list_books')),  # 👈 redirect / → /books/
    path('', include('LibraryProject.relationship_app.urls')),
]
