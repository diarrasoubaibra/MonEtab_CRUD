from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

from django.contrib.auth.models import User
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            return render (request, 'user/add.html')
        
        user = User(username=username)
        user.save()
        user.password = password
        user.set_password(user.password)
        user.save()
        login(request, user)
        return redirect('user:list')
    
    return render (request, 'add.html')

def user(request):
    users = User.objects.all()
    return render(request, "user/list.html", {'users': users})

def add(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('user:list')
    else:
        user_form = UserForm()
    return render(request, "user/add.html", {'user_form':user_form})

def edit(request, pk):
    if request.method == "POST":
        user = User.objects.get(id=pk)
        user_form =UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('user:list')
    else:
        user = User.objects.get(id=pk)
        users = UserForm(instance=user)
        
        return render(request, "user/edit.html", {'users':users})
    
def delete(request, pk):
    teacher = User.objects.get(id=pk)
    teacher.delete()
    
    return redirect('user:list')