from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpRequest
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template.loader import render_to_string
from women.models import Women, Category, TagPost
from django.template.defaultfilters import slugify #импортируем любой фильтр
from women.forms import AddPostForm

#menu = ['о сайте', 'Добавить статью', 'Обратная связь', 'Войти']

menu2=[
    {'title':'о сайте', 'url_name':'women:about'},
    {'title':'Добавить статью', 'url_name':'women:addpage'},
    {'title':'Обратная связь', 'url_name':'women:contact'},
    {'title':'Войти', 'url_name':'women:login'},
    
]

cats_db=[
    {"id":"1", "name":"Actrisi"},
    {"id":"2", "name":"Pevici"},
    {"id":"3", "name":"Sport women"},
]

def index(request):
    #t=render_to_string('women/index.html')
    title='Главная страница'
    data=[
        {'id':'1','title':'Qwerty','description':'qwert qwe qwe System check identified no issues (0 silenced).'
'''January 22, 2025 - 08:20:45
Django version 3.2.25, using settings 
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.''', 'is_published':True},
        {'id':'2','title':'2Qwerty','description':'2qwert qwe qwe', 'is_published':False},
        {'id':'3','title':'3Qwerty','description':'3qwert qwe qwe', 'is_published':True},
    ]

    data2 = {
        'form_data': {'is_data': True, 'username': 'root', 'password': '1234'},
    }

    #posts=Women.objects.filter(is_published=1)
    posts=Women.published.all().select_related("cat")
    context={
        'title':title,
        #'menu':menu,
        #'posts':data,
        'data2':data2,
        'menu2':menu2,
        'cat_selected':0,
        'posts':posts,
    }
    #return HttpResponse("Page index")
    #return HttpResponse(t)
    return render(request, 'women/index.html', context)

def about(request):
    title='o сайте'
    float=23.5
    int=24
    #url=slugify("Моя статья")
    data={
        'title':title,
        #'menu':menu,
        'float':float,
        'int':int,
        'url':slugify("My page"),
        'menu2':menu2,
    }
    return render(request, "women/about.html", context=data)

def categories(request, cat_id):
    print(request.GET)
    context={

    }
    return HttpResponse(f"<h2>Categories</h2><p>id:{cat_id}</p>")

def categories_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    context={

    }
    return HttpResponse(f"<h2>Categories</h2><p>clug:{cat_slug}</p>")

def arhive(request, year):
    if year > 2023:
        raise Http404()
    if year == 2000:
        return redirect('women:categories_slug', 'Dodic')
    if year == 2001:
        return redirect('index', permanent=True)
    if year == 2012:
        uri=reverse('women:categories_slug', args=('Music',))
        return redirect(uri)
    if year == 2022:
        uri=reverse('women:categories_slug', args=('SDDS',))
        return HttpResponseRedirect(uri)
    if year == 2015:
        uri=reverse('index', args=('IIIIIII',))
        return HttpResponsePermanentRedirect(uri)
    return HttpResponse(f"<h2>Categories</h2><p>year:{year}</p>")

def post_detail(request):
    if request.GET:
        print(request.GET)
        return HttpResponse("|".join([f'{k}={v}' for k, v in request.GET.items()]))
        return HttpResponse('yes')
    else:
        return HttpRequest('GET is empty')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h2>Страница не найдена</h2>")

def show_post(request, sp_slug):
    post1=get_object_or_404(Women, slug=sp_slug)
    print(post1.slug)
    data={
        'title':post1.title,
        'menu2':menu2,
        'post1':post1,
        'cat_selected':1,
    }
    return render(request,"women/show_post.html",data)
    #return HttpResponse(f"Post id={post_id}")

def addpage(request):
    #return HttpResponse(f"Add post")
    if request.method=="POST":
        form=AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect("women:index")
            except:
                form.add_error(None, "Fatal create post")
    else:
        form=AddPostForm()
    context={
        'menu':menu2,
        'title':'ADD page',
        'form':form,
    }
    return render(request,"women/addpage.html",context)

def contact(request):
    return HttpResponse(f"Contact - обратная связь")

def login(request):
    return HttpResponse(f"Login")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h2>Page Not Found</h2>")

def show_category(request, cat_slug):
    category=get_object_or_404(Category, slug=cat_slug)
    posts=Women.published.filter(cat_id=category.pk).select_related("cat")
    data={
        'title':f'Rubrica {category.name}',
        'menu2':menu2,
        #'posts':data2,
        #'cat_selected':cat_id,
        'cat_selected':category.pk,
        'category':category,
        'posts':posts,
    }
    #return index(request)
    return render(request, 'women/index.html', context=data)

def show_tag_postlist(request, tag_slug):
    tag=get_object_or_404(TagPost, slug=tag_slug)
    posts=tag.tags.filter(is_published=Women.Status.PUBLISHED)
    data={
        'title':f'Tag: {tag.tag}',
        'menu2':menu2,
        'posts':posts,
        'cat_selected': None
    }
    return render(request, 'women/index.html', context=data)
