from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
from django.conf import settings
import os


# Create your models here.
class Post(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(_('title'), max_length=255),
        content=models.TextField(_('content'))
    )
    imageUrl = models.URLField(verbose_name=('Image URL'), blank=True, null=True)
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name=('Publication Date'))

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.title

# Create schema for whoosh

schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True), path=ID(stored=True))

# Ensure Whoosh index is exists

if not os.path.exists(settings.WHOOSH_INDEX):
    os.mkdir(settings.WHOOSH_INDEX)
if not index.exists_in(settings.WHOOSH_INDEX):
    ix = index.create_in(settings.WHOOSH_INDEX, schema)
else:
    ix = index.open_dir(settings.WHOOSH_INDEX)

# Signal to update the Whoosh index when a Post is saved or deleted
@receiver(post_save, sender=Post)
def update_post_index(sender, instance, **kwargs):
    try:
        writer = ix.writer()
        writer.update_document(title=instance.title, content=instance.content, path='/post/' + str(instance.id))
        writer.commit()
    except Exception as e:
        print(f"Error updating index: {e}")

@receiver(post_delete, sender=Post)
def delete_post_index(sender, instance, **kwargs):
    try:
        writer = ix.writer()
        writer.delete_by_term('path', '/post/' + str(instance.id))
        writer.commit()
    except Exception as e:
        print(f"Error deleting from index: {e}")
