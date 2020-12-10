from django.db import models as db
from django.contrib.auth.admin import User
from django.utils import timezone


class Tag(db.Model):
    name = db.CharField(max_length=30, verbose_name='Name')
    slug = db.SlugField(max_length=50, default='', blank=False)

    class Meta:
        verbose_name = 'Tags'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('blog:tag', kwargs={'slug': self.slug})


class Category(db.Model):
    """Категория"""
    name = db.CharField("Категория", max_length=50)
    description = db.TextField("Описание")
    url = db.SlugField("Ссылка", max_length=60, unique=True)


    def __str__(self):
        return self.url

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return f"/blog/{self.url}/"

        

class Post(db.Model):
    """Посты"""
    image = db.FileField("Фото", upload_to='uploads/%Y_%m_%d/')
    title = db.CharField("Название", max_length=50)
    intro = db.TextField("Введение", max_length=200)
    text = db.TextField("Описание")
    url = db.SlugField("Ссылка", max_length=60, unique=True)
    draft = db.BooleanField("Черновик")
    author = db.ForeignKey(
        User, verbose_name = "Имя ползователя и статус", on_delete=db.SET_NULL, null=True
    )
    category = db.ForeignKey(
        Category, verbose_name = "Категория", on_delete=db.SET_NULL, null=True
    )
    tag = db.ManyToManyField(Tag, verbose_name='Tags')

    date = db.DateTimeField("Дата", default=timezone.now)


    def __str__(self):
        return self.title

    def get_intro(self):
        return self.text[:200]

    def get_absolute_url(self):
        """Получаем обсолютную ссылку""" 
        return f"/blog/{self.category}/{self.url}/"



    # def get_review(self):
    #     return self.reviews_set.filter(parent__isnull=True)

    def get_user_status(self):
        if self.author.is_staff and self.author.is_superuser:
            return "Admin"

    def del_url(self):
        """Получаем обсолютную ссылку с id для удаления"""
        return f"/mini-admin/delete/{self.category}/{self.id}/"

    def draft_url(self):
        """Получаем обсолютную ссылку с id для удаления"""
        return f"/mini-admin/drafter/{self.category}/{self.id}/"

    def edit_url(self):
        """Получаем обсолютную ссылку с id для удаления"""
        return f"/mini-admin/edit/{self.category}/{self.id}/"

    def GetTags(self):
        # get all Tag objects for this Article.
        return Post.objects.get(id=self.id).tag.all()


    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"