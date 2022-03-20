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
    pre_comment = models.ForeignKey('self',on_delete=models.DO_NOTHING,null=True,verbose_name='father_id')  #if no father set to NULL, "self"foreign to self

    def save(self, *args, **kwargs):
        if len(self.comment_text) <= 0 or self.comment_text.isspace():
            self.comment_text = "invalid comment input"
        super(Comment, self).save(*args, **kwargs)