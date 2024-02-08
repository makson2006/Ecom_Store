from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from store.forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


def category(request,foo):
    foo = foo.replace('-', ' ')

    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request,'store/category.html', {'products':products,'category':category})
    except:
        messages.success(request, ("That Category Doesn't exist"))
        return redirect('home')

def home(request):
    products = Product.objects.all()
    return render(request, "store/home.html", {'products':products})

def about(request):
    return render(request, "store/about.html", {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged Successfully"))
            return redirect('home')
        else:
            messages.success(request, ('Wrong username or password'))
            return redirect('login')
    else:
        return render(request,'store/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out..."))
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have Registered succesfully..."))
            return redirect('home')
        else:
            messages.success(request, ("There is some problems with your username or password or username can be busy..."))
            return redirect('register')

    else:
        return render(request, "store/register.html", {'form': form})


def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, "store/product.html", {'product':product})

