from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('blogs/', views.blog, name='blogs'),
    path('users/', views.users, name='users'),
    path('categories/', views.categories, name='categories'),
    path('blogs/blogdetails/<int:id>', views.blog_detail, name='details'),
    path('comments/', views.comments, name='comments')
]
