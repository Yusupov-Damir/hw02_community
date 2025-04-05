from tempfile import template
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from .models import Post, Group

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    current_year = datetime.now().year
    context = {
        'posts' : posts,
        'current_year' : current_year,
    }
    return render(request, 'posts/index.html', context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug = slug)
    posts = Post.objects.filter(group = group).order_by('-pub_date')[:10]
    current_year = datetime.now().year
    context = {
        'group': group,
        'posts': posts,
        'current_year': current_year,
    }
    return render(request, 'posts/group_list.html', context)