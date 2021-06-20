from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title         # model objects are now shown with their title in admin section and shell

    def snippet(self):
        return self.body[:80]+'...'
#python manage.py makemigrations
#puthon manage.py migrate