import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, resolve_url
from theme.forms import ArticleThemeForm, ArticleForm,commentForm
from django.urls import reverse
from . import models


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

@login_required
@csrf_exempt
def commentViews(request):
    if request.method == 'POST':
        comment_user = request.user
        comment_text = request.POST.get('text','')
        comment_atricle = request.POST.get('comment_atricle','')

        comment = models.Comment()
        comment.comment_user = comment_user
        comment.comment_text = comment_text
        comment.comment_article = comment_atricle
        comment.save()
        return redirect(reverse('theme:comment'))
    else:
        article_comment_list = request.user.artheme_set.all()
        return render(request,'article/comment.html',{'article_comment_list':article_comment_list})






#   form = commentForm()
#    if request.method == 'POST':
#        form.save(commit=True)
#        return JsonResponse({"err_msg": "successful!"}, safe=False)
#    else:
#        article_comment_list = request.user.artheme_set.all()
#       return render(request,'article/comment.html',{'article_comment_list':article_comment_list})
