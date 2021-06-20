from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.Articles_List, name="list"),   #home page
    path('create/', views.Article_create, name="create"),
    url(r'^(?P<slug1>[\w-]+)/$', views.Article_detail, name="detail"),
]
