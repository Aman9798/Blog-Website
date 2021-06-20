from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
# Create your views here.
def Articles_List(request):
    article_objects = Article.objects.all().order_by('date')
    return render (request, 'articles/ArticlesList.html', {'articles' : article_objects}) # sendind data in dictionary form

def Article_detail(request, slug1):
    #return HttpResponse(slug1)
    article_object = Article.objects.get(slug=slug1) 
    return render (request, 'articles/ArticleDetail.html', {'details' : article_object})