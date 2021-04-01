from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from blog.models import Post, Category, Tag
from main.models import Visitor

   
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return Visitor(ip=ip, url=request.path).save()


class MainView(View):
    """Основная страница"""

    def get(self, request):

    	# Филтруеть посты если пост не черновык то выведёт пост
        query = Post.objects.filter(draft=False).order_by('-date')
        categories = Category.objects.all()
       
        

        return render(request, 'main/index.html',
    		{'nav_name': 'Основная страница',
            'post_list': query,
            'view': {'category': categories},
            'get_tags': Tag.objects.order_by('-id')})


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

def logout_view(request):
    logout(request)
    return redirect('/')

class Search(ListView):
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(
            title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context

class QTag(ListView):
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(
            tag__name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context