from django.contrib import admin
from .models import User, Post, Comment, Category

class UserAdmin(admin.ModelAdmin):
    list_display = ("id","username", "email", "password")

admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)

