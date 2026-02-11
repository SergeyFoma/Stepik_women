from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound

# from django.template.loader import render_to_string

from women.models import Women


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    # t=render_to_string('women/index.html')
    # return HttpResponse(t)
    posts = Women.objects.filter(is_published=1)
    context = {
        "title": "Главная страница",
        "menu": menu,
        "posts": posts,
    }
    return render(request, "women/index.html", context)


def categories(request, cat_id):
    # cat_id=int(555)
    # return HttpResponse(f"<h2>Статьи по категориям</h2><p>id: {cat_id}</p>")
    return render(request, "women/categories.html", {"cat_id": cat_id})


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    # cat_slug=str()
    context = {
        "cat_slug": cat_slug,
    }
    return HttpResponse(f"SLUG: {context}")


def show_post(request, post_slug):
    pos = get_object_or_404(Women, slug=post_slug)
    title = "POST"
    context = {
        "title": title,
        "menu": menu,
        "pos": pos,
        "cat_selected": 1,
    }
    return render(request, "women/show_post.html", context)


def page_not_found(request, exception):
    print("exception: ", exception)
    return HttpResponseNotFound("<h1>Page not found. Страница не существует.</h1>")
