from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/index.html", context)


def about(request):
    context = {"title": "About"}
    return render(request, "blog/about.html", context)
