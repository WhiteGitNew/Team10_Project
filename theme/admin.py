from django.contrib import admin

# Register your models here.
from theme.models import Article, Artheme, like

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_id', 'article_author')

class ArthemeAdmin(admin.ModelAdmin):
    list_display = ('at_id', 'at_author', 'at_name')

class likeAdmin(admin.ModelAdmin):
    list_display = ('like_id', 'like_poster_id', 'like_article_id')

admin.site.register(Artheme, ArthemeAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(like, likeAdmin)