from django.urls import path, re_path, register_converter
from women import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

app_name="women"

urlpatterns=[
    #path('', views.index, name='index'),
    path('',views.IndexView.as_view(),name='index'),
    path('about/', views.about, name='about'),
    path('categories/<int:cat_id>/', views.categories, name='categories'),
    path('categories_slug/<slug:cat_slug>/', views.categories_slug, name='categories_slug'),
    #re_path(r'^arhive/(?P<year>[0-9]{4})',views.arhive, name='arhive'),
    path('arhive/<year4:year>/', views.arhive, name='arhive'),
    path('post_detail/', views.post_detail, name='post_detail'),
    path('show_post/<slug:sp_slug>/', views.show_post, name='show_post'),
    #path('addpage/', views.addpage, name='addpage'),
    path('addpage/',views.AddPage.as_view(),name='addpage'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    #path('show_category/<slug:cat_slug>/', views.show_category, name="show_category"),
    path('show_category/<slug:cat_slug>/', views.ShowCategory.as_view(), name="show_category"),
    path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag'),
]