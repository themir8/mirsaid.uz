from modeltranslation.translator import register, TranslationOptions
from .models import Post, Category, Tag


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'intro', 'text')