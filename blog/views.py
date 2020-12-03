from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def home(request):
    post = Post.objects.all()


    context = {
        'post': post,
    }
    return render(request, 'blog/home.html', context)