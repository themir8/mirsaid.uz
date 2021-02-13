from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.models import User
from .models import Profile


class ProfileView(View):
    """Профиль ползователя"""

    def get(self, request):

        query = User.objects.get(username=request.user.username)

        return render(request, 'user/index.html', {'user': query})
    def post(self, request):
    	if(not request.user.is_authenticated):
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
