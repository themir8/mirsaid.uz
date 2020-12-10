from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Post, Category, Tag


class TagAdmin(admin.ModelAdmin):
    pass


class PostAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    text = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	"""docstring for PostAdmin"""
	list_display = ('id', 'name', 'url')
	list_display_links = ('name',)
	search_fields = ('name',)
	save_as = True

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'draft', 'date')
	list_display_links = ('title',)
	list_filter = ('date', 'draft')
	list_editable = ('draft',)
	search_fields = ('title',)
	save_as = True
	readonly_fields = ('date',)
	form = PostAdminForm


admin.site.register(Tag, TagAdmin)

admin.site.site_title='mirsaid.uz'
admin.site.site_header='mirsaid.uz'
# admin.site.index_title='mirsaid.uz'