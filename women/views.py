from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string


def index(request):
    # t=render_to_string('women/index.html')
    # return HttpResponse(t)
    return render(request, "women/index.html", {})


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


def page_not_found(request, exception):
    print('exception: ', exception)
    return HttpResponseNotFound("<h1>Page not found. Страница не существует.</h1>")

