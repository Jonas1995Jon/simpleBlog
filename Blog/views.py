from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()
    content = {"articles": articles}
    return render(request, 'Blog/index.html', content)

def article_page(request, articleID):
    article = Article.objects.get(id=articleID)
    content = {'article': article}
    return render(request, 'Blog/article_page.html', content)

def edit_page(request, articleID):
    if str(articleID) == '0':
        return render(request, 'Blog/edit_page.html')
    article = Article.objects.get(id=articleID)
    content = {'article': article}
    return render(request, 'Blog/edit_page.html', content)

def edit_action(request):
    articleID = request.POST.get('articleID', '0')
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    Article.objects.create(title=title, content=content)
    articles = Article.objects.all()
    return render(request, 'Blog/index.html', {'articles': articles})