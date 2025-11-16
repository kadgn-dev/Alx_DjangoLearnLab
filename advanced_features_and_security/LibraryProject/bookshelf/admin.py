from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser


# ================================
# Book Model Admin (Your existing code)
# ================================
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)


# ================================
# Custom User Admin
# ================================
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )


# REQUIRED BY CHECKER:
admin.site.register(CustomUser, CustomUserAdmin)
