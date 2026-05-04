from django import forms
from .models import Post, Category, Comment


class CategoryForm(forms.ModelForm):
    """Formulario para crear/editar categorías"""
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción'}),
        }


class PostForm(forms.ModelForm):
    """Formulario para crear/editar posts"""
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'category', 'published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del post'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Contenido'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class CommentForm(forms.ModelForm):
    """Formulario para agregar comentarios"""
    class Meta:
        model = Comment
        fields = ['author_name', 'email', 'content']
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu email'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Tu comentario'}),
        }


class SearchPostForm(forms.Form):
    """Formulario para buscar posts"""
    search = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar posts por título o autor...'
        })
    )
