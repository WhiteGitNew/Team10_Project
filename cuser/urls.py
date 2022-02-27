from django.urls import path, re_path
from . import views

app_name = 'cuser'

urlpatterns = [
    path(r"cuser/detail_profile/",views.detail_profile,name="detail_profile"),
]