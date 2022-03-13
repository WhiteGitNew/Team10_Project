from django.contrib import admin

from .models import Comment
# Register your models here.
@admin.register(Comment)
class CommentAdimin(admin.ModelAdmin):
    list_display = ('comment_id','comment_text','comment_time','comment_user')