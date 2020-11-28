from django import forms
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from blog.models import Post, Category, Tag


class TagView:
    def get_tags(self):
        return Tag.objects.order_by('-id')


class MainView(TagView, View):
    """Основная страница"""
    def get(self, request):

    	# Филтруеть посты если пост не черновык то выведёт пост
        query = Post.objects.filter(draft=False).order_by('-date')[:3]
        categories = Category.objects.all()
        
        return render(request, 'main/index.html',
    		{'title': 'Основная страница',
            'nav_name': 'Основная страница',
            'post_list': query,
            'category': categories})
            # 'tag_list': Tag.objects.order_by('-id')})


def Registration(request):
    if(not request.user.is_authenticated):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                return HttpResponseRedirect("/")
        else:
            form = UserCreationForm()
        return render(request, "main/registration.html", {
            'form': form,
            })
    else:
       return HttpResponseRedirect("/") 


def LoginView(request):
    if(not request.user.is_authenticated):
        if request.method == "POST":
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            
            user = authenticate(
                username=username,
                password=password
                )
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/account/invalid/")
    else:
           return HttpResponseRedirect("/") 
    
    return render(request, 'main/login.html')


class Search(ListView):
    """Поиск фильмов"""
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(
            title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context