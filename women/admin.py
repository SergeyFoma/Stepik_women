from django.contrib import admin, messages
from women.models import Women, Category, TagPost
from django.utils.safestring import mark_safe


class MarriedFilter(admin.SimpleListFilter):
    title='Статус женщин'
    parameter_name='status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)

@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields=['title','slug','content','photo','post_photo','cat','husband','tags']
    readonly_fields=['post_photo']
    list_display = ["id", "title","post_photo","slug","cat", "time_create", "is_published","active","brief_info"]#отображаемые поля
    list_display_links = ['id', 'title'] #кликабельные поля
    prepopulated_fields={'slug':('title',)}
    ordering=['time_create', 'title']
    list_editable=('is_published','cat') #редактируемые поля
    list_per_page=3 #максимальное число записей на страницу
    actions=['set_published','set_draft']
    search_fields=['title','cat__name']
    list_filter=[MarriedFilter,'cat__name','is_published']
    save_on_top=True

    @admin.display(description="Изображение", ordering='content')
    def post_photo(self, women:Women):
        if women.photo:
            return mark_safe(f"<img src='{women.photo.url}'width=50>")
        return "Без фото"

    @admin.display(description="Краткое описание", ordering='content')
    def brief_info(self, women:Women):
        return f"Описание {len(women.content)} символов"

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count=queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count=queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f"{count} записей снято с публикации", messages.WARNING)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'slug']
    list_display_links=['id', 'name']
    prepopulated_fields={'slug':('name',)}

#admin.site.register(Category, CategoryAdmin)

