from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Текст статьи')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего редактирования')
    is_published = models.BooleanField(default=True, verbose_name='Опубликована')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья о женщине'
        verbose_name_plural = 'Статьи о женщинах'
        ordering = ['-time_create']  # сортируем статьи по убыванию даты создания
