from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django import views
# Create your views here.

class Signup_view(views.View):
    def get(self,request):
        form=UserCreationForm()
        return render(request,template_name='app2/signup.html',context={'form':form})

    def post(self,request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
        return render(request,template_name='app2/signup.html',context={'form':form})

class Login_view(views.View):
    def get(self,request):
        return render(request,template_name='app2/login.html',context={})
    def post(self,request):
        u=request.POST.get('un')
        p=request.POST.get('pw')
        user=authenticate(username=u,password=p)
        if user is not None:
            login(request, user)
            return redirect('show_url')
        return render(request, template_name='app2/login.html', context={})


class Logout_view(views.View):
    def get(self,request):
        logout(request)
        return redirect('login_url')