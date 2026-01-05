from django.shortcuts import render,redirect
from blogs .models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogPostForm,AddUserForm,EditUserForm
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
# Create your views here.


'''here dashboard view is projected only for admin users(staff and superuser) using login required decorator and checking user permissions inside the view function,number of categories and blogs are counted using the ORM and passed to the template for display'''
@login_required(login_url='login')
def dashboard(request):
    if not request.user.is_staff and not request.user.is_superuser:
        messages.error(request, "You do not have permission to access the dashboard.")
        return redirect('home') 
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {
        "category_count": category_count,
        "blogs_count": blogs_count,
    }
    return render(request, 'dashboard/dashboard.html', context)

'''in dashboard app category management views are created for adding,editing,deleting and viewing categories using category model and category form'''
def category(request):
    return render(request,'dashboard/categories.html')


# add category view
def add_category(request):
    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm()
    context={"form":form}
    return render(request,'dashboard/add_category.html',context)

# edit category view
def edit_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    if request.method=="POST":
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm(instance=category)
    context={"form":form,
             "category":category,}
    return render(request,'dashboard/edit_category.html',context)

# delete category view
def delete_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')

'''in dashboard app post management views are created for adding ,editing and deleting posts using blog model and blog post form'''
def posts(request):
    posts=Blog.objects.all()
    context={"posts":posts}
    return render(request,'dashboard/post.html',context)

# add post view
def add_posts(request):
    if request.method=="POST":
        form=BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            posts=form.save(commit=False)
            posts.author=request.user 
            posts.save()
            title=form.cleaned_data['title']
            posts.slug=slugify(title) + '-'+ str(posts.id)
            posts.save()
            return redirect('posts')
    form=BlogPostForm()
    context={"form":form}
    return render(request,'dashboard/add_post.html',context)

# edit post view
def edit_posts(request,pk):
    post=get_object_or_404(Blog,pk=pk)
    if request.method=="POST":
        form=BlogPostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post=form.save()
            title=form.cleaned_data['title']
            post.slug=slugify(title) + '-' +str(post.id)
            post.save()
            return redirect('posts')
    form=BlogPostForm(instance=post)
    context={"form":form, 'post':post}
    return render(request,'dashboard/edit_post.html',context)

# delete post view
def delete_posts(request,pk):
    post=get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('posts')

'''in dashboard app user views are created for adding,deleting and  editing users using django built in  user model and custom user forms'''
def users(request):
    users=User.objects.all()
    context={"users":users}
    return render(request,'dashboard/users.html',context)

# add user view
def add_user(request):
    if request.method=="POST":
        form=AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    form=AddUserForm()
    context={"form":form}
    return render(request,'dashboard/add_user.html',context)

# edit user view
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users') 
    else:
        form = EditUserForm(instance=user)
    context = {
        "form": form,
        "user": user
    }   
    return render(request, 'dashboard/edit_user.html', context)

# delete user view
def delete_user(request,pk):
    user=get_object_or_404(User,pk=pk)
    user.delete()
    return redirect('users')