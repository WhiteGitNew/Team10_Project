from distutils.command.upload import upload
import os

from django import views
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project_forum.settings')

import django
django.setup()
from comment.models import Comment
from theme.models import Artheme
from theme.models import Article
from django.contrib.auth.models import User
def populate():
    
    
    
    user4 = [{
        'user_id':4,
        'username': 'Jinddsdfa',
        'password': '523434fdsfsed',
        'email': '453@qq.com'
    }]
    user3 = [{
        'user_id':3,
        'username': 'yongddsgtren',
        'password': 'GUYGH12345',
        'email': '454@qq.com'
    }]

    java_comments_one =[
        {'comment_id':3,
        'comment_user':user3,
         'comment_text':"NullPointerExceptions are exceptions that occur when you try to use a reference that points to no location in memory (null) as though it were referencing an object. Calling a method on a null reference or trying to access a field of a null reference will trigger a NullPointerException. These are the most common, but other ways are listed on the NullPointerException javadoc page.",
         'count_all_liked':20,
         'count_all_collected':10},
         {'comment_id':4,
         'comment_user':user4,
          'comment_text': "In Java, the java.lang.NullPointerException is thrown when a reference variable is accessed (or de-referenced) and is not pointing to any object. This error can be resolved by using a try-catch block or an if-else condition to check if a reference variable is null before dereferencing it.",
         'count_all_liked':10,
         'count_all_collected':30}
    ]
    user6 = [{
        'user_id':6,
        'username': 'Jina',
        'password': '523434fdsfsed',
        'email': '453@qq.com'
    }]

    java_articles = [
        {'article_id':2,
         'article_author': user6,
         'comment': java_comments_one,
         'article_title':'What is a NullPointerException, and how do I fix it?',
         'article_content':"What are Null Pointer Exceptions (java.lang.NullPointerException) and what causes them? What methods/tools can be used to determine the cause so that you stop the exception from causing the program to terminate prematurely?",
         'count_all_liked':20,
         'count_all_commented':2}
    ]
    
   
   
    user2 = [{
        'user_id':2,
        'username': 'Arya',
        'password': '523434fdsfsed',
        'email': '544950896@qq.com'
    }]
    user1 = [{
        'user_id':1,
        'username': 'Yongsendd',
        'password': 'GUYGH12345',
        'email': '123456@qq.com'
    }]
    python_comments_one =[
        {'comment_id':1,
         'comment_user':user1,
         'comment_text':"This is a really useful example and I'll be using it as a base for examples. Many thanks!",
         'count_all_liked':20,
         'count_all_collected':10},
         {'comment_id':2,
        'comment_user':user2,
         'comment_text':'If you copy the output of printing, most of the time answerers can use read_clipboard()... except for MultiIndex :s. Saying that, dict is good addition ',
         'count_all_liked':9,
         'count_all_collected':30}
    ]
    user5 = [{
        'user_id':5,
        'username':'yongsen',
        'password': 'GUYGH12345',
        'email': '454@qq.com'
    }]
    python_articles = [
        {'article_id':1,
         'article_author': user5,
         'comment': python_comments_one,
         'article_title':'How to make good reproducible pandas examples?',
         'article_content':'How can we create good reproducible examples for pandas questions?',
         'count_all_liked':1,
         'count_all_commented':2
         }
    ]
    user7 = [{
        'user_id':7,
        'username': 'ddd',
        'password': 'GUYGH12345',
        'email': '3243234@qq.com'
    }]
    user8 = [{
        'user_id':8,
        'username': 'Bojo',
        'password': '523434fdsfsed',
        'email': '674334@qq.com'
    }]
    themes = {
            'Python': {
                'at_id':1,
                'at_name':'Python',
                'article': python_articles,
                'authors': user7,
                'at_cover':'/upload/theme/111_vBzcj3H.jpg', 
                'at_count':20
            },
            'Java': {
                'at_id':2,
                'at_name':'Java',
                'article': java_articles,
                'authors': user8,
                'at_cover':'/upload/theme/111_2hGp7df.jpg', 
                'at_count':20
                }
            }
    for cat, cat_data in themes.items():

        for tu in cat_data['authors']:
            add_user(tu['user_id'],tu['username'],tu['password'],tu['email'])  
        add_cat(tu['user_id'],cat_data['at_id'],cat_data['at_name'],cat_data['at_cover'],cat_data['at_count'])


        for p in cat_data['article']:
            for u in p['article_author']:
                add_user(u['user_id'],u['username'],u['password'],u['email'])
                add_article(p['article_id'],cat_data['at_id'],u['user_id'],p['article_title'],p['article_content'],p['count_all_liked'],p['count_all_commented'])
            
            for ac in p['comment']:
                for uu in ac['comment_user']:
                    add_user(uu['user_id'],uu['username'],uu['password'],uu['email'])
                    add_comment(ac['comment_id'],p['article_id'],uu['user_id'],ac['comment_text'],ac['count_all_liked'],ac['count_all_collected'])


def add_comment(comment_id,article_id, author_id, content, likes=0, countComment=0):
        q = Comment.objects.get_or_create(comment_id=comment_id,article_id=article_id,comment_user_id = author_id)[0]
        q.comment_text = content
        q.count_all_liked = likes
        q.count_all_commented = countComment
        q.save()
        return q

def add_article(article_id, article_theme_id, author_id,article_title, article_content, likes=0, countComment=0):
        p = Article.objects.get_or_create(article_id=article_id,article_author_id = author_id,article_theme_id=article_theme_id)[0]
        p.article_title = article_title
        p.article_content = article_content
        p.count_all_liked = likes
        p.count_all_commented = countComment
        p.save()
        return p

def add_cat(author_id,id, name, at_cover,at_count=0):
        c = Artheme.objects.get_or_create(at_id = id,at_author_id = author_id)[0]
        c.at_name=name
        c.at_cover = at_cover
        c.at_count = at_count
        c.save()
        return c

def add_user(user_id,username,password,email):
        u = User.objects.get_or_create(id=user_id,username = username,password = password,email = email)
        return u

# Start execution here!
if __name__ == '__main__':
    print('Starting team10 population script...')
    populate()
