from unicodedata import name
from django.urls import path, re_path
from . import views


app_name = "comment"

urlpatterns = [
    # re_path(r"add/", views.user_comment, name="user_comment"),
    re_path(r"detail/(?P<article_id>\d+)", views.article_detail, name="article_detail"),
    path('comment_control/',views.comment_control,name='comment_control')
]