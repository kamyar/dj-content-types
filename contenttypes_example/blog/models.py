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

    def __str__(self):
        return "{}".format(self.id)
class Article(models.Model):
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    tags = GenericRelation('Tag')

    title = models.CharField(max_length=80, blank=True)
    body = models.TextField(blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "{obj.id} {obj.title}".format(obj=self)

class Photo(models.Model):
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    tags = GenericRelation('Tag')

    image = models.ImageField()
    title = models.CharField(max_length=80, blank=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return "{obj.id} {obj.title}".format(obj=self)
