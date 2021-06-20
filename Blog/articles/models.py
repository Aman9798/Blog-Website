from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_DEFAULT

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=SET_DEFAULT)

    def __str__(self):
        return self.title         # model objects are now shown with their title in admin section and shell

    def snippet(self):
        return self.body[:80]+'...'
#python manage.py makemigrations
#puthon manage.py migrate