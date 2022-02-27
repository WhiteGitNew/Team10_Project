from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    up_id = models.AutoField(verbose_name="userprofile_id", primary_key=True)
    count_subject = models.IntegerField(verbose_name="theme number", default=0)
    count_collected = models.IntegerField(verbose_name="collect number", default=0)
    count_liked = models.IntegerField(verbose_name="like person number", default=0)
    count_article = models.IntegerField(verbose_name="publish article number", default=0)
    user = models.OneToOneField(verbose_name="belong to user", to=User, on_delete=models.CASCADE)
    author = models.OneToOneField(verbose_name="which author focused", to=User, on_delete=models.SET_NULL,
                                  blank=True, null=True, related_name='author')
    authors = models.ManyToManyField(verbose_name="focused which author", to=User,related_name='authors')
