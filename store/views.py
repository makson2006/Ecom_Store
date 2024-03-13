import os

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Books
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from store.forms import SignUpForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


def download_book(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    # Припустимо, що поле 'file' у вашій моделі містить шлях до файлу книги
    with open(book.file.path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf') # Змініть content_type на тип вашого файлу
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(book.file.path)
        return response


def category(request,foo):
    foo = foo.replace('-', ' ')

    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        books = Books.objects.filter(category=category)
        return render(request,'store/category.html', {'products':products,'category':category,'books':books})
    except:
        messages.success(request, ("That Category Doesn't exist"))
        return redirect('home')

def all_products(request):
    all_books = Books.objects.all()
    products = Product.objects.all()
    return render(request, "store/all_products.html", {'products':products,'all_books':all_books})

def books(request):
    all_books = Books.objects.all()
    return render(request, 'store/all_books.html',{'all_books':all_books,})

def book(request,pk):
    book = Books.objects.get(id=pk)
    return render(request, "store/book.html", {'book':book})


def home(request):
    return render(request, "store/home.html", {})

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

