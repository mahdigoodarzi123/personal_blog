from django.shortcuts import render
from .models import Post

def main(request):
    posts = Post.objects.filter(active=1).order_by('-created_time')
    context = {'posts':posts}
    return render(request , 'blog/main.html', context=context)


def about(request):
    return render(request, "blog/about.html")


def single_post(request, num):
    posts = Post.objects.filter(active = 1, pk = num)
    context = {'posts':posts}
    return render(request, 'blog/post.html', context=context)