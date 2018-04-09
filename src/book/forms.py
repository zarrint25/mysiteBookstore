from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'book_name','writer','genre','review','publisher','price','document'
        ]
