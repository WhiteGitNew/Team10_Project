from django.urls import path, re_path
from . import views

app_name = "theme"

urlpatterns = [
    path(r"article_theme_add/", views.article_theme_add, name="article_theme_add"),
    path(r"article_publish/", views.article_publish, name="article_publish"),
    path(r"comment/", views.commentViews, name="comment"),
]