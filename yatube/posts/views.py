from tempfile import template
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Group

@login_required  #Защита маршрута с помощью декоратора login_required.
def index(request):
    post_list = Post.objects.all().order_by('-pub_date')  # Запрос к модели.
    paginator = Paginator(post_list, 10)  # Показывать по 10 записей на странице.
    page_number = request.GET.get('page')  # Из URL извлекаем номер запрошенной страницы - page.
    page_obj = paginator.get_page(page_number)  # Получаем набор записей для страницы с запрошенным номером.
    context = {
        'page_obj' : page_obj,
    }
    return render(request, 'posts/index.html', context)

@login_required
def group_posts(request, slug):
    group = get_object_or_404(Group, slug = slug)
    post_list = Post.objects.all().filter(group = group).order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)