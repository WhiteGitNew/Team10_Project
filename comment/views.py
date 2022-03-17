from pydoc import resolve
from django.http import JsonResponse
from django.shortcuts import render, redirect, resolve_url
from .models import Comment
from django.urls import reverse
from django.contrib import messages

# Create your views here.


from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from theme.models import Article


# def user_comment(request):
#
#     return render(request,"article/publish_ar_detail.html")

def article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    comment_list = Comment.objects.filter(article_id = article_id)
    context = {
        'article' : article,
        'comment_list' : comment_list
    }
    return render(request, "article/publish_ar_detail.html", context=context)

@login_required
@csrf_exempt
def comment_control(request): 
    if request.user.username:
        comment_user = request.user
        comment_text = request.POST.get('text','')

        article_id = request.POST.get('article_id')
        article = Article.objects.filter(article_id = article_id)[0]

        if len(comment_text) == 0 or comment_text.isspace() :
            print('输入无效评论')
            messages.error(request,"Please enter valid content!")
            return redirect('/comment/detail/'+ article_id)

        pid = request.POST.get('pid')
        Comment.objects.create(comment_text=comment_text,pre_comment_id=pid,article_id=article_id,comment_user=comment_user)

        # show the comment
        article.count_all_commented = Comment.objects.filter(article = article).count()
        article.save()

        print('输入评论有效')
        # article = list(Comment.objects.values('comment_id','comment_text','pre_comment_id','article_id','comment_user','comment_time'))
        return redirect(resolve_url("commonly:index"))
    #else:
    #    return redirect('/user_login/')
