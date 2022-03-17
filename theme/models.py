from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artheme(models.Model):
    """theme"""
    at_id = models.AutoField(verbose_name="theme id", primary_key=True)
    at_author = models.ForeignKey(verbose_name="belong to which user", to=User, on_delete=models.CASCADE)
    at_name = models.CharField(verbose_name="theme name", max_length=50)
    at_count = models.IntegerField(verbose_name="have how many articles", default=0)
    at_cover = models.ImageField(verbose_name="theme cover picture", upload_to="upload/theme/")
    authors = models.ManyToManyField(verbose_name="which user subscribed", to=User, related_name="article_theme")


class Article(models.Model):
    """article"""
    article_id = models.AutoField(verbose_name="article id", primary_key=True)
    article_author = models.ForeignKey(verbose_name="belong to which user", to=User, on_delete=models.CASCADE)
    article_theme = models.ForeignKey(verbose_name="belong to which theme", to=Artheme, on_delete=models.CASCADE)
    article_content = models.TextField(verbose_name="publish content")
    publish_time = models.DateField(verbose_name="publish time", auto_now_add=True)
    article_title = models.CharField(verbose_name="article title", max_length=200)
    article_img = models.ImageField(verbose_name="article cover image", upload_to="upload/ar/", default="/media/upload/ar/moren.jpg")

    count_all_liked = models.IntegerField(verbose_name="how many person liked", default=0)
    count_all_collected = models.IntegerField(verbose_name="how many person collected", default=0)
    count_all_commented = models.IntegerField(verbose_name="how many person commented", default=0)
    count_all_words = models.IntegerField(verbose_name="count article words", default=0)

    def __str__(self) -> str:
        return self.article_title + "-" + self.article_content

class like(models.Model):
    """like"""
    like_id = models.AutoField(verbose_name="like id", primary_key=True)
    like_poster_id = models.IntegerField(verbose_name="like poster id")
    like_article_id = models.IntegerField(verbose_name="liked article")

