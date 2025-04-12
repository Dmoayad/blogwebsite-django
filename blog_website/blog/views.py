from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User, Comment, Post, Category

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def blog(request):
    myposts = Post.objects.all().values()
    template = loader.get_template('blogs.html')
    context = {
        'myposts': myposts,
    }
    return HttpResponse(template.render(context, request))

def comments(request):
    mycomments = Comment.objects.all()
    template = loader.get_template('comments.html')
    context = {
        'mycomments': mycomments,
    }
    return HttpResponse(template.render(context, request))

def categories(request):
    mycats = Category.objects.all().values()
    template = loader.get_template('categories.html')
    context = {
        'mycats': mycats,
    }
    return HttpResponse(template.render(context, request))

def blog_detail(request, id):
    mydetails = Post.objects.get(id=id)
    template = loader.get_template('blogdetails.html')
    context = {
        'mydetails': mydetails,
    }
    return HttpResponse(template.render(context, request))

def users(request):
    myusers = User.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'myusers': myusers,
    }
    return HttpResponse(template.render(context, request))