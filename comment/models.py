from django.db import models
from django.contrib.auth.models import User
from theme.models import Article

# Create your models here.
class Comment(models.Model):
    article = models.ForeignKey(verbose_name="belong to which article", to=Article, on_delete=models.CASCADE)
    comment_id = models.AutoField(verbose_name="comment id", primary_key=True)
    comment_text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    count_all_liked = models.IntegerField(verbose_name="how many person liked", default=0)
    count_all_collected = models.IntegerField(verbose_name="how many person collected", default=0)
    pre_comment = models.ForeignKey('self',on_delete=models.DO_NOTHING,null=True,verbose_name='父评论id')  #父级评论，如果没有父级则为空NULL, "self"表示外键关联自己