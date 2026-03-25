from django.shortcuts import render, redirect
from .models import Article
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    articles = Article.objects.all()
    return render(request, "blog/index.html", {"articles":articles})

def detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, "blog/detail.html", {"article":article})