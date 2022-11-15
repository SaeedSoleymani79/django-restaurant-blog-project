from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("",views.blog_list,name="blog_list"),
    path("<int:id>",views.blog_details,name="blog_details"),
    path("tag/<slug:tag>",views.search_tag,name="tag"),
    path("category/<slug:category>",views.search_category,name="category"),
    path("search/",views.search,name="search"),
]