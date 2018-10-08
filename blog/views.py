from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from blog.models import Blog
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
User = get_user_model()
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    blog_list = Blog.objects.all().order_by('-create_date')
    paginator = Paginator(blog_list, 5)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'index.html',{'posts': posts})


def about(request):
    return render(request, 'about.html',locals())

def detail(request, url):
    val = Blog.objects.get(slug = url)
    return render(request, 'detail.html',locals())


def logout_view(request):
    logout(request)
    redirect('index')
