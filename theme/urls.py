from unicodedata import name
from django.urls import path, re_path
from . import views

app_name = "theme"

urlpatterns = [
    path(r"article_theme_add/", views.article_theme_add, name="article_theme_add"),
    path(r"article_publish/", views.article_publish, name="article_publish"),
    re_path(r"author_articles/(?P<author_id>\d+)/$", views.author_articles, name="author_articles"),
    re_path(r"theme_details/(?P<at_id>\d+)/$", views.theme_details, name="theme_details"),
]