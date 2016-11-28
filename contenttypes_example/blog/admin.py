
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline,GenericStackedInline


from .models import Tag, Article, Photo

class TagInline(GenericTabularInline):
    model = Tag
    extra = 0
    can_delete = True

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "term", "nedir_bu"]
    def nedir_bu(self, obj):
        content_model = obj.content_type.model_class()
        content_model_obj = content_model.objects.get(id=obj.object_id)
        return "{} > {}".format(content_model.__name__, content_model_obj)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInline]

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    inlines = [TagInline]


