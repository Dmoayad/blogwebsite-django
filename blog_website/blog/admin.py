from django.contrib import admin
from .models import User, Post, Comment, Category

class UserAdmin(admin.ModelAdmin):
    list_display = ("id","username", "email", "password")

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "category", "date_published")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "post_id", "user_id", "content", "date_posted")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)

