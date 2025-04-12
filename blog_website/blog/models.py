from datetime import datetime

from django.db import models
from django.db.models import SET_NULL
from django.contrib.auth.hashers import make_password, check_password


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def set_password(self, raw_password):
        """Hashes and stores the password with validation"""
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def save(self, *args, **kwargs):
        """Ensure password is hashed before saving"""
        if not self.password.startswith(('pbkdf2_','pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)

    def verify_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.id} {self.username}"

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    category = models.ForeignKey('Category', default=None, null=True, on_delete=SET_NULL)
    date_published = models.DateTimeField(default=datetime.now(), null=True, blank=True)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    date_posted = models.DateTimeField(auto_now=True)




class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    # def __str__(self):
    #     return f"{self.name}"
