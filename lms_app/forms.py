from django import forms
from .models import Book, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model= Category
        fields= ['name']
        widgets ={
            'name' : forms.TextInput(attrs={'class': 'form-control'})
        }



class BookForm(forms.ModelForm):
    class Meta:
        model= Book
        fields = [
            'title', 'author', 'photo_book', 'photo_author', 
            'pages', 'price', 'rental_price_day', 'rental_period', 
            'total_rental_price', 'status', 'category'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'photo_book': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'photo_author': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'rental_price_day': forms.NumberInput(attrs={'class': 'form-control', 'id': 'rental_price_day'}),
            'rental_period': forms.NumberInput(attrs={'class': 'form-control', 'id': 'rental_period'}),
            'total_rental_price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'total_rental_price'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }