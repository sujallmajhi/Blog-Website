from django.shortcuts import render,redirect
from blogs.models import Category,Blog
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth 
from django.core.paginator import Paginator

# create your views here  
''' home page view '''
def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-created_at')
    posts=Blog.objects.filter(is_featured=False,status='Published').order_by('-created_at')
    paginator = Paginator(posts, 2) 
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number) 
    context={
        'featured_posts':featured_posts,
        'posts':posts
    }
    return render(request,'home.html',context)


'''user registration view'''
def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect('home')
        else:
            print(form.errors)
    else:
        form=RegistrationForm()
    context={"form":form}
    return render(request,'register.html',context)

'''user login view'''
def login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
    form=AuthenticationForm()
    context={"form":form}
    return render(request,'login.html',context)

'''user logout view'''
def logout(request):
    auth.logout(request)
    return redirect('home')