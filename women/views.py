from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpRequest
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template.loader import render_to_string
from women.models import Women, Category, TagPost, UploadFiles
from django.template.defaultfilters import slugify #импортируем любой фильтр
from women.forms import AddPostForm
from .forms import UploadFileForm
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from women.utils import DataMixin
from django.core.paginator import Paginator

#menu = ['о сайте', 'Добавить статью', 'Обратная связь', 'Войти']

# menu2=[
#     {'title':'о сайте', 'url_name':'women:about'},
#     {'title':'Добавить статью', 'url_name':'women:addpage'},
#     {'title':'Обратная связь', 'url_name':'women:contact'},
#     {'title':'Войти', 'url_name':'women:login'},
    
# ]

cats_db=[
    {"id":"1", "name":"Actrisi"},
    {"id":"2", "name":"Pevici"},
    {"id":"3", "name":"Sport women"},
]

# def index(request):
#     #t=render_to_string('women/index.html')
#     title='Главная страница'
#     data=[
#         {'id':'1','title':'Qwerty','description':'qwert qwe qwe System check identified no issues (0 silenced).'
# '''January 22, 2025 - 08:20:45
# Django version 3.2.25, using settings 
# Starting development server at http://127.0.0.1:8000/
# Quit the server with CTRL-BREAK.''', 'is_published':True},
#         {'id':'2','title':'2Qwerty','description':'2qwert qwe qwe', 'is_published':False},
#         {'id':'3','title':'3Qwerty','description':'3qwert qwe qwe', 'is_published':True},
#     ]

#     data2 = {
#         'form_data': {'is_data': True, 'username': 'root', 'password': '1234'},
#     }

#     #posts=Women.objects.filter(is_published=1)
#     posts=Women.published.all().select_related("cat")
#     context={
#         'title':title,
#         #'menu':menu,
#         #'posts':data,
#         'data2':data2,
#         'menu2':menu2,
#         'cat_selected':0,
#         'posts':posts,
#     }
#     #return HttpResponse("Page index")
#     #return HttpResponse(t)
#     return render(request, 'women/index.html', context)

# class IndexView(TemplateView):
#     template_name='women/index.html'
#     # extra_context={
#     #     'title':'Главная страница',
#     #     'menu2':menu2,
#     #     'posts':Women.published.all().select_related("cat"),
#     #     'cat_selected':0,
#     # }

#     def get_context_data(self,**kwargs):
#         context=super().get_context_data(**kwargs)
#         context['title']='Главнейшая страница'
#         context['menu2']=menu2
#         context['posts']=Women.published.all().select_related("cat")
#         context['cat_selected']=int(self.request.GET.get('cat_id',0))
#         return context

class IndexView(DataMixin,ListView):
    #model=Women
    template_name='women/index.html'
    context_object_name='posts'
    #если mixin
    title_page='Главная страница'
    cat_selected=0
    #paginate_by=5 #перенесли в DataMixin
    # extra_context={
    #     'title':'Главная страница',
    #     'menu2':menu2,
    #     'posts':Women.published.all().select_related("cat"),
    #     'cat_selected':0,
    # }

    # def get_context_data(self, **kwargs):
    #     context=super().get_context_data(**kwargs)
    #     context['title']="Главненькая страничка"
    #     context['menu2']=menu2
    #     context['posts']=Women.published.all().select_related("cat")
    #     context['cat_selected']=int(self.request.GET.get('cat_id',0))
    #     return context
    
    def get_queryset(self):
        return Women.published.all().select_related("cat")


#метод для загрузки файлов
def handle_uploaded_file(f):
    with open(f"uploads/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def about(request):
    contact_list=Women.published.all()
    paginator=Paginator(contact_list, 3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    if request.method=="POST":
        form=UploadFileForm(request.POST, request.FILES)
        #handle_uploaded_file(request.FILES['file_upload'])
        if form.is_valid():
            #handle_uploaded_file(form.cleaned_data['file'])#для forms.Form
            fp=UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form=UploadFileForm()
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
        #'menu2':menu2,
        "form":form,
        'page_obj':page_obj,
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

# def show_post(request, sp_slug):
#     post1=get_object_or_404(Women, slug=sp_slug)
#     print(post1.slug)
#     data={
#         'title':post1.title,
#         'menu2':menu2,
#         'post1':post1,
#         'cat_selected':1,
#     }
#     return render(request,"women/show_post.html",data)
#     #return HttpResponse(f"Post id={post_id}")

# class ShowPost(DetailView):
#     model=Women
#     template_name="women/show_post.html"
#     slug_url_kwarg='sp_slug'
#     context_object_name='post1'
#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         context['title']=context['post1'].title
#         context['menu2']=menu2
#         return context
#     def get_object(self, queryset=None):
#         return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwarg])

class ShowPost(DataMixin, DetailView):
    #model=Women
    template_name="women/show_post.html"
    slug_url_kwarg="sp_slug"
    context_object_name="post1"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['post1'].title)
        # context['title']=context['post1'].title
        # context['menu2']=menu2
        # return context
    def get_object(self, queryset=None):
        return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwarg])

# def addpage(request):
#     #return HttpResponse(f"Add post")
#     if request.method=="POST":
#         form=AddPostForm(request.POST,request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # Это для formFoms
#             # try:
#             #     Women.objects.create(**form.cleaned_data)
#             #     return redirect("women:index")
#             # except:
#             #     form.add_error(None, "Fatal create post")
#             form.save()
#             return redirect("women:index")
#     else:
#         form=AddPostForm()
#     context={
#         'menu':menu2,
#         'title':'ADD page',
#         'form':form,
#     }
#     return render(request,"women/addpage.html",context)


# class AddPage(View):
#     def get(self, request):
#         form=AddPostForm()
#         context={
#             'menu':menu2,
#             'title':'AddPage',
#             'form':form
#         }
#         return render(request,"women/addpage.html",context)

#     def post(self, request):
#         form=AddPostForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("women:index")
#         context={
#             'menu':menu2,
#             'title':'AddPage',
#             'form':form
#         }
#         return render(request,"women/addpage.html",context)

# class AddPage(FormView):
#     form_class=AddPostForm
#     template_name="women/addpage.html"
#     success_url=reverse_lazy("women:index")
#     extra_context={
#         'title':'Добавить статью',
#         'menu2':menu2,
#     }
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

class AddPage(DataMixin, CreateView):
    form_class=AddPostForm
    model=Women
    #fields='__all__'
    template_name="women/addpage.html"
    #success_url=reverse_lazy("women:index")
    # extra_context={
    #     'title':'Добавить статью',
    #     'menu2':menu2,
    # }
    #DataMixin
    title_page='Добавить статью'

class UpdataPage(DataMixin, UpdateView):
    model=Women
    fields=['title', 'content', 'photo', 'is_published', 'cat']
    template_name="women/addpage.html"
    success_url=reverse_lazy("women:index")
    # extra_context={
    #     'title':'Редактировать статью',
    #     'menu2':menu2,
    # }
    #DataMixin
    title_page="Редактировать статью"

class DeletePage(DeleteView):
    model=Women
    template_name="women/deletepage.html"
    success_url=reverse_lazy("women:index")


def contact(request):
    return HttpResponse(f"Contact - обратная связь")

def login(request):
    return HttpResponse(f"Login")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h2>Page Not Found</h2>")

# def show_category(request, cat_slug):
#     category=get_object_or_404(Category, slug=cat_slug)
#     posts=Women.published.filter(cat_id=category.pk).select_related("cat")
#     data={
#         'title':f'Rubrica {category.name}',
#         'menu2':menu2,
#         #'posts':data2,
#         #'cat_selected':cat_id,
#         'cat_selected':category.pk,
#         'category':category,
#         'posts':posts,
#     }
#     #return index(request)
#     return render(request, 'women/index.html', context=data)

class ShowCategory(DataMixin, ListView):
    template_name='women/index.html'
    context_object_name="posts"
    allow_empty=False
    #paginate_by=5 #перенесли в DataMixin
    def get_queryset(self):
        return Women.published.filter(cat__slug=self.kwargs['cat_slug']).select_related("cat")
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cat=context['posts'][0].cat
        # context['title']='Категория - ' + cat.name
        # context['menu2']=menu2
        # context['cat_selected'] = cat.pk
        # return context
        return self.get_mixin_context(context,
                        title='Категория - ' + cat.name,
                        cat_selected=cat.pk)

    

# def show_tag_postlist(request, tag_slug):
#     tag=get_object_or_404(TagPost, slug=tag_slug)
#     posts=tag.tags.filter(is_published=Women.Status.PUBLISHED)
#     data={
#         'title':f'Tag: {tag.tag}',
#         'menu2':menu2,
#         'posts':posts,
#         'cat_selected': None
#     }
#     return render(request, 'women/index.html', context=data)

class ShowTagPostlist(DataMixin, ListView):
    template_name='women/index.html'
    context_object_name='posts'
    allow_empty=False
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        tag=TagPost.objects.get(slug=self.kwargs['tag_slug'])
        # context['title']=f'Tag: {tag.tag}'
        # context['menu2']=menu2
        # #context['posts']=posts
        # context['cat_selected']=None
        # return context

        #DataMixin
        return self.get_mixin_context(context, title='Тег - ' + tag.tag)

    def get_queryset(self):
        return Women.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')
