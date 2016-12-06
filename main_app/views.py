from django.shortcuts import render
from .models import Post, Comment
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def post_headers(request):
    
    post_list = Post.objects.all()

    paginator = Paginator(post_list, 3)

    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)    



    dic_info ={     
        "posts": posts,
    }



    return render(request, "post_headers.html", dic_info)


def post_text(request, post_id):
    
    post = Post.objects.get(id = post_id)    
    
    comment_list = Comment.objects.filter(post_id = post)
    
    paginator = Paginator(comment_list, 6)
    
    page = request.GET.get('page')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        comments = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        comments = paginator.page(paginator.num_pages)    
        

    dic_info ={     
        "post_text": post.post_text,
        "post": post,
        "comments": comments,
    }

    return render(request, "post_text.html", dic_info)    