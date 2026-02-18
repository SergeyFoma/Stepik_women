from django.contrib import admin

from .models import Women, Category, TagPost  # импортируем нашу модель Women

# Регистрируем модель через декоратор
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    fields=['title', 'content', 'slug', 'tags']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    fields=['name', 'slug']

@admin.register(TagPost)
class TagPostAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('tag',)}
    fields=['tag', 'slug']

