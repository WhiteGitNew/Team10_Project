from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.


from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from theme.models import Article


# def user_comment(request):
#
#     return render(request,"article/publish_ar_detail.html")

def article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, "article/publish_ar_detail.html", {"article": article})