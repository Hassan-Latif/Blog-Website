from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='default.png',blank=True)

    def __str__(self):
        return self.title
    def snippets(self):
        return self.body[:110]+ '...'