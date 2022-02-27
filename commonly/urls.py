from django.urls import path, re_path
from . import views

app_name = 'commonly'

urlpatterns = [
    path(r"index/", views.index, name="index"),
]