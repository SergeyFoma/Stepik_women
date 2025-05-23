from django import template
import women.views as views
from women.models import Category, TagPost
from django.db.models import Count
from women.utils import menu2

register = template.Library()

@register.simple_tag
def get_menu():
    return menu2

#@register.simple_tag()
@register.simple_tag(name="getcats")
def get_categories():
    return views.cats_db

@register.inclusion_tag("women/list_categories.html")
def show_categories(cat_selected=0):
    #cats=views.cats_db
    #cats=Category.objects.all()
    cats=Category.objects.annotate(total=Count('posts')).filter(total__gt=0)
    return {"cats":cats, "cat_selected":cat_selected}

@register.inclusion_tag("women/list_tags.html")
def show_all_tags():
    #return {"tags":TagPost.objects.all()}
    return {"tags":TagPost.objects.annotate(total=Count("tags")).filter(total__gt=0)}