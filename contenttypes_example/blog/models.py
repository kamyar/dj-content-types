from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

# Assign the User model in case it has been "swapped"
User = settings.AUTH_USER_MODEL


class Tag(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    term = models.CharField(max_length=30)


class Article(models.Model):
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    tags = GenericRelation('Tag')

    title = models.TextField(blank=True)
    body = models.TextField(blank=True)


    class Meta:
        ordering = ('created',)



class Photo(models.Model):
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    tags = GenericRelation('Tag')

    image = models.ImageField()
    title = models.TextField(blank=True)

    class Meta:
        ordering = ('created',)
