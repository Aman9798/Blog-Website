from django.shortcuts import redirect, render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def Articles_List(request):
    article_objects = Article.objects.all().order_by('date')
    return render (request, 'articles/ArticlesList.html', {'articles' : article_objects}) # sendind data in dictionary form

def Article_detail(request, slug1):
    #return HttpResponse(slug1)
    article_object = Article.objects.get(slug=slug1) 
    return render (request, 'articles/ArticleDetail.html', {'details' : article_object})

@login_required(login_url="/accounts/login/")
def Article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article
            instance1 = form.save(commit=False)  # returns the instance just before saving the form
            instance1.author = request.user         # attachs the user with form
            instance1.save()     # finally saves it
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render (request, 'articles/ArticleCreate.html', {'form': form})
   # return HttpResponse("ngnik ")