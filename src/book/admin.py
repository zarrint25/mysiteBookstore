from django.contrib import admin
from .models import Book, Publisher, Writer

admin.site.register(Book)
admin.site.register(Writer)
admin.site.register(Publisher)

# Register your models here.
