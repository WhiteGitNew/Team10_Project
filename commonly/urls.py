from django.urls import path, re_path
from . import views
import commonly

app_name = 'commonly'

urlpatterns = [
    path(r"index/", views.index, name="index"),
    re_path(r"index/(?P<article_id>\d+)/$", views.article_like, name="article_like"),
]