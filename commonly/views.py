from django.views.decorators.http import require_POST,require_GET
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from django.contrib import messages
from theme.models import Artheme, Article, like


# Create your views here.

def index(request):
    all_themes = Artheme.objects.all()[:10]
    all_article = Article.objects.all()[:10]
    return render(request,"index.html",{'all_themes':all_themes,'all_article':all_article})

@login_required
@require_GET
def article_like(request, article_id):
    article = Article.objects.filter(article_id = article_id)[0]
    likesOfArticle = like.objects.filter(like_article_id = article_id)

    for like_temp in likesOfArticle:
        if like_temp.like_poster_id == request.user.id:
            # currenct user has already posted a like to target article
            messages.info(request, "you have canceled a like.")
            like_temp.delete()
            article.count_all_liked -= 1
            article.save()
            return redirect(resolve_url('commonly:index'))

    # user haven't posted a like to target article before
    like.objects.create(like_poster_id = request.user.id, like_article_id = article_id)
    messages.info(request, "you just posted a like!")
    article.count_all_liked += 1
    article.save()

    return redirect(resolve_url("commonly:index"))