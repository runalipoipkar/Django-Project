from django.shortcuts import render,redirect
from .forms import PersonForm
from .models import Person
from django import views
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(login_required(login_url='login_url'),name='dispatch')
class Add_view(views.View):
    def get(self,request):
        form=PersonForm()
        return render(request,template_name='app1/add.html',context={'form':form})
    def post(self,request):
        form=PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
        return render(request,template_name='app1/add.html',context={'form':form})


@method_decorator(login_required(login_url='log_url'),name='dispatch')
class Show_view(views.View):
    def get(self,request):
        data=Person.objects.all()
        return render(request,template_name='app1/show.html',context={'data':data})


class Update_view(views.View):
    def get(self,request,pk):
        data=Person.objects.get(id=pk)
        form=PersonForm(instance=data)
        return render(request,template_name='app1/add.html',context={'form':form})

    def post(self,request,pk):
        data = Person.objects.get(id=pk)
        form = PersonForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('show_url')
        return render(request, template_name='app1/add.html', context={'form': form})


class Delete_view(views.View):
    def get(self,request,pk):
        data = Person.objects.get(id=pk)
        data.delete()
        return redirect('show_url')



