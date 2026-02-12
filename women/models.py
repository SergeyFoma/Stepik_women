from django.db import models
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
    slug=models.SlugField(max_length=100, db_index=True, unique=True, verbose_name='Slug')

    def __str__(self):
        return self.name

class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug=models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL') #https://docs.djangoproject.com/en/6.0/ref/models/fields/#slugfield
    content = models.TextField(verbose_name='Текст статьи')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего редактирования')
    is_published = models.BooleanField(default=True, verbose_name='Опубликована')
    cat=models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория',blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья о женщине'
        verbose_name_plural = 'Статьи о женщинах'
        ordering = ['-time_create']  # сортируем статьи по убыванию даты создания https://docs.djangoproject.com/en/6.0/ref/models/options/#django.db.models.Options.ordering
        indexes = [
            models.Index(fields=['-time_create',]),
    
        ]

    def get_absolute_url(self): # https://docs.djangoproject.com/en/6.0/ref/models/instances/#:~:text=get_absolute_url%28%29
        return reverse("women:show_post", kwargs={"post_slug": self.slug})
    
    
