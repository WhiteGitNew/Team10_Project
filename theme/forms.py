from django import forms
from . import models

class ArticleThemeForm(forms.ModelForm):
    class Meta:
        model = models.Artheme
        fields = ["at_name", "at_cover", "at_author"]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ["article_title", "article_content", "article_author", "article_theme"]


class commentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ["comment_user","comment_text"]
        #fields = ["comment_user","comment_text",'comment_article']