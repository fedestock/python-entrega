from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Post, Category, Comment
from .forms import PostForm, CategoryForm, CommentForm, SearchPostForm


def index(request):
    """Vista principal - listado de posts"""
    posts = Post.objects.filter(published=True)
    categories = Category.objects.all()
    search_form = SearchPostForm(request.GET)
    
    if search_form.is_valid() and search_form.cleaned_data['search']:
        search_term = search_form.cleaned_data['search']
        posts = posts.filter(
            Q(title__icontains=search_term) | 
            Q(author__icontains=search_term)
        )
    
    context = {
        'posts': posts,
        'categories': categories,
        'search_form': search_form,
    }
    return render(request, 'index.html', context)


def post_detail(request, pk):
    """Vista detalle de un post"""
    post = get_object_or_404(Post, pk=pk, published=True)
    comments = post.comments.filter(approved=True)
    comment_form = CommentForm()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, '¡Comentario agregado exitosamente!')
            return redirect('post_detail', pk=pk)
    
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'post_detail.html', context)


def category_posts(request, pk):
    """Vista de posts por categoría"""
    category = get_object_or_404(Category, pk=pk)
    posts = category.posts.filter(published=True)
    
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'category_posts.html', context)


def create_post(request):
    """Vista para crear un nuevo post"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Post creado exitosamente!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    
    context = {'form': form, 'title': 'Crear Post'}
    return render(request, 'create_post.html', context)


def create_category(request):
    """Vista para crear una nueva categoría"""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, 'Categoría creada exitosamente!')
            return redirect('index')
    else:
        form = CategoryForm()
    
    context = {'form': form, 'title': 'Crear Categoría'}
    return render(request, 'create_category.html', context)


def create_comment(request):
    """Vista para crear un comentario (por si se llama directamente)"""
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comentario creado!')
            return redirect('index')
    else:
        form = CommentForm()
    
    context = {'form': form, 'title': 'Agregar Comentario'}
    return render(request, 'create_comment.html', context)


def all_categories(request):
    """Vista para listar todas las categorías"""
    categories = Category.objects.all()
    
    context = {'categories': categories}
    return render(request, 'all_categories.html', context)


def all_posts(request):
    """Vista para listar todos los posts"""
    posts = Post.objects.filter(published=True)
    search_form = SearchPostForm(request.GET)
    
    if search_form.is_valid() and search_form.cleaned_data['search']:
        search_term = search_form.cleaned_data['search']
        posts = posts.filter(
            Q(title__icontains=search_term) | 
            Q(author__icontains=search_term)
        )
    
    context = {
        'posts': posts,
        'search_form': search_form,
    }
    return render(request, 'all_posts.html', context)
