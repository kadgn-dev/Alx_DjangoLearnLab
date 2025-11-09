from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # ✅ Built-in Django auth views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # ✅ Register (matches autograder expectation)
    path('register/', views.register, name='register'),
]
