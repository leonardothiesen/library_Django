from django.contrib import admin
from .models import Books, Genres

class BooksAdmin(admin.ModelAdmin):
    list_display = ['name','genre','pages','cover','author','copies']
    list_filter = ['name','genre','author']
    search_fields = ['name','genre','author']

admin.site.register(Books, BooksAdmin)
admin.site.register(Genres)