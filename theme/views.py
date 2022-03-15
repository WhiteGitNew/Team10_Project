from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST,require_GET
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from theme.forms import ArticleThemeForm, ArticleForm
from django.contrib.auth.models import User




@login_required
@require_POST
def article_theme_add(request):
    _form = ArticleThemeForm(request.POST, request.FILES)
    if _form.is_valid():
        _form.save()
    return redirect(resolve_url("commonly:index"))

@login_required
@csrf_exempt
def article_publish(request):
    if request.method == "GET":
        article_theme_list = request.user.artheme_set.all()
        return render(request, "article/publish_ar.html",
                      {"article_theme_list": article_theme_list})
    elif request.method == "POST":
        article_form = ArticleForm(request.POST)
        article_form.save()
    return JsonResponse({"err_msg": "successful!"}, safe=False)


    # search all articles of authors
@require_GET
def author_articles(request, author_id):
    author = User.objects.get(pk=author_id)
    return render(request, "article/author_article.html", {"author": author})