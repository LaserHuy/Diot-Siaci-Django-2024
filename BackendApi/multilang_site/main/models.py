from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Post(models.Model):
    title = models.CharField(_('title') ,max_length=200)
    content = models.TextField(_('content'))
    imageUrl = models.URLField(verbose_name=('Image URL'))
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name=('Publication Date'))

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.title