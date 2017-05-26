# coding: utf-8
from django.shortcuts import render
from blog.models import Post


def register(request):
    post_list = Post.objects.all().order_by('-create_time')
    for i in post_list:
        print i.title
    return render(request, 'index.html', context={'title': '注册页面', 'post_list': post_list})