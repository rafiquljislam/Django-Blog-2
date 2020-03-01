from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login,logout
# Create your views here.


def home(request):
    posts = Post.objects.all()

    letsgo={
        'posts':posts
    }

    return render(request,'home/home.html',letsgo)


def contact(request):
    messages.info(request, 'Welcome to Contact.')
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        textarea = request.POST['textarea']
        if len(fname) <3 or len(lname)< 3 or len(email) < 4 or len(textarea) <5:
            messages.warning(request, "Please fill the form correctly")
        else:
            contact = Comment(fname=fname,lname=lname,email=email,commentsss=textarea)
            contact.save()
            messages.success(request, "Your massege has been send !")

    return render(request,'home/contact.html')

def search(request):
    search_cont = request.GET['quary']

    if len(search_cont) > 50:
        allpost = Post.objects.none()
    else:
        allposttitle = Post.objects.filter(title__contains = search_cont)
        allpostcontent = Post.objects.filter(content__contains = search_cont)
        allpost = allposttitle.union(allpostcontent)
    if len(allpost) == 0:
        messages.info(request, "Please fill the form correctly !")
    letsgo={
        'allpost':allpost,
        'search_cont':search_cont
    }


    return render(request,'home/search.html',letsgo)

def blogpost(request,slug):
    posts = Post.objects.filter(slug=slug)[0]
    blogpost={
        'post':posts,
    }
    return render(request,'home/blogpost.html',blogpost)

def singup1(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if len(username) > 70:
            messages.warning(request,'Username is Big')
            return redirect('home')
        if password1 != password2:
            messages.warning(request,"User Password is not match")
            return redirect('home')
        if not username.isalnum():
            messages.warning(request, "Username must be text and creaccter !")
            return redirect('home')
        myuser = User.objects.create_user(username=username,email=email,password=password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'Your Account has been Created !')
        return redirect('home')

    else:
        return HttpResponse("404--Page not Found")
            
def loginnow(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, 'Successfully Loged in !')
        return redirect('home')
    else:
        messages.success(request, 'Invited Input !')
        return redirect('home')
            
def logoutnow(request):
    logout(request)
    messages.success(request, 'Successfully Loged Out !')
    return redirect('home')