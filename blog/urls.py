from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/<int:pk>/', views.category_posts, name='category_posts'),
    path('crear-post/', views.create_post, name='create_post'),
    path('crear-categoria/', views.create_category, name='create_category'),
    path('crear-comentario/', views.create_comment, name='create_comment'),
    path('categorias/', views.all_categories, name='all_categories'),
    path('posts/', views.all_posts, name='all_posts'),
]
