from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class PublisheManager(models.Manager):
    def get_queryset(self):
        #return super().get_queryset().filter(is_published=1)
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)

class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title=models.CharField(max_length=100,verbose_name='Название',unique=True)
    slug=models.SlugField(max_length=100, unique=True, db_index=True)
    photo=models.ImageField(upload_to="photos/%Y/%m/%d", default=None, blank=True, null=True, verbose_name="Фото")
    content=models.TextField(verbose_name='Текст', blank=True)
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    #is_published=models.BooleanField(default=True)
    #is_published=models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    is_published=models.BooleanField(choices=tuple(map(lambda x:(bool(x[0]),x[1]),Status.choices)),
                                default=Status.DRAFT, verbose_name='Статус')
    #cat=models.ForeignKey(to='Category', on_delete=models.PROTECT, null=True)
    cat=models.ForeignKey(to='Category', on_delete=models.PROTECT, related_name='posts')
    tags=models.ManyToManyField(to='TagPost', blank=True, related_name='tags')
    husband=models.OneToOneField('Husband', on_delete=models.SET_NULL, null=True,
                        blank=True, related_name='women')
    active=models.BooleanField(default=True)
    author=models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,related_name='posts',null=True,default=None)

    objects=models.Manager()
    published=PublisheManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Известные женщины'
        verbose_name_plural='Известные женщины'
        ordering=['-time_create']
        indexes=[
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('women:show_post',kwargs={'sp_slug':self.slug})

class Category(models.Model):
    name=models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug=models.SlugField(max_length=100, unique=True, db_index=True)

    class Meta:
        verbose_name='Категорию'
        verbose_name_plural='Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('women:show_category', kwargs={'cat_slug':self.slug})

class TagPost(models.Model):
    tag=models.CharField(max_length=100, db_index=True)
    slug=models.SlugField(max_length=100, db_index=True, unique=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('women:tag', kwargs={'tag_slug':self.slug})

class Husband(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(null=True)
    n_count=models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name



class UploadFiles(models.Model):
    file=models.FileField(upload_to="uploads_model")