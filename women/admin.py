from django.contrib import admin

<<<<<<< HEAD
from women.models import Women

@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    pass
=======
from .models import Women  # импортируем нашу модель Women

# Регистрируем модель через декоратор
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
>>>>>>> new_branch
