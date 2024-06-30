from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.
class Post(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=255),
        content=models.TextField(_('content'))
    )
    imageUrl = models.URLField(verbose_name=('Image URL'))
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name=('Publication Date'))

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.title