from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name=('Title'))
    content = models.TextField(verbose_name=('Content'))
    imageUrl = models.URLField(verbose_name=('Image URL'))
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name=('Publication Date'))

    def __str__(self):
        return self.title