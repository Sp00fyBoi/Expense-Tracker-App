from django.contrib import admin
from .models import Book, BookCategory

admin.site.register(BookCategory)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'publisher', 'published_date', 'distribution_expense')
    list_filter = ('category',)
    search_fields = ('title', 'authors')

admin.site.register(Book, BookAdmin)

