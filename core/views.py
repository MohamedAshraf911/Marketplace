from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from item.models import Category, Item
from django.contrib.auth.models import User

from .forms import SignupForm, LoginForm
from core.decorator import unauthenticated_user

def index(request):
    items = Item.objects.filter(is_Sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # user1= form.save(commit=False)
            # user = User(username = user1.username,email=user1.email,password=user1.password)
            # user.save(using='database2')
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    
    return render(request,'core/signup.html',{
        'form': form
    })

# def login(request):
#     # future -> ?next=/articles/create/
#     if request.method == "POST":
#         form = LoginForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('/')
#     else:
#         form = LoginForm(request)
#     context = {
#         "form": form
#     }
#     return render(request, "core/login.html", context)


def logout(request):
    if request.method == "POST":
        
        return redirect("/logout/")
    return render(request, "core/logout.html", {})
