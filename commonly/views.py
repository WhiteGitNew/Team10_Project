from django.shortcuts import render
from theme.models import Artheme, Article


# Create your views here.

def index(request):
    all_themes = Artheme.objects.all()[:10]
    all_article = Article.objects.all()[:10]
    print(request.path)
    return render(request,"index.html",{'all_themes':all_themes,'all_article':all_article})

