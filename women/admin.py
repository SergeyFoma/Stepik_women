from django.contrib import admin

from .models import Women  # импортируем нашу модель Women

# Регистрируем модель через декоратор
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
