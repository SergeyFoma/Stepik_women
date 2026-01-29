from django.urls import path
from . import views
from women.views import categories#, page_not_found

app_name = "women"

urlpatterns = [
    path("", views.index, name="index"),
    path("cat/<int:cat_id>/", categories, name="categories"),
    path("cat/<slug:cat_slug>/", views.categories_by_slug, name="categories_by_slug"),
]

#handler404 = page_not_found
