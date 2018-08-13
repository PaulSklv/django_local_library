from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language
from django.contrib.auth.models import User
# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Genre)
# admin.site.register(BookInstance)
class BookInLine(admin.TabularInline):
	model = Book
	extra = 0
	fields = ['title', 'genre', 'language']

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
	inlines = [BookInLine]

admin.site.register(Author, AuthorAdmin)

class BooksInstanceInLine(admin.TabularInline):
	model = BookInstance
	extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	inlines = [BooksInstanceInLine]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	list_display = ('book', 'status', 'borrower', 'due_back')
	list_filter = ('status', 'due_back')

	fieldsets = (
		(None, {'fields': ('book', 'imprint', 'id')}),
		('Availability', {'classes': ('collapse',), 'fields': ('status', 'due_back', 'borrower')}),
	)


