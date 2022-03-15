from django.contrib import admin

# Register your models here.
from .models import Comment
# Register your models here.
@admin.register(Comment)
class CommentAdimin(admin.ModelAdmin):
    list_display = ('comment_id','comment_text','comment_time','comment_user','article')