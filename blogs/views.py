
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Blog,Category,Comment
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.

#fetch the posts based on category id passed from url and render the post in category template with pagination
def post_by_category(request, category_id):
    keyword = request.GET.get('keyword')
    posts_list = Blog.objects.filter(status='Published', category=category_id).order_by('-created_at')
    if keyword:
        posts_list = posts_list.filter(title__icontains=keyword)
    category = get_object_or_404(Category, pk=category_id)
    paginator = Paginator(posts_list, 2) 
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number) 
    context = {
        "posts": posts,
        "category": category,
        "keyword": keyword  
    }
    return render(request, 'post_by_category.html', context)

'''blog detail view with comment functionality where user can add comment to specific blog'''
def blog(request,slug):
    first_post=get_object_or_404(Blog,slug=slug,status='Published')
    if request.method=="POST":
        comment=Comment()
        comment.user=request.user
        comment.blog=first_post
        comment.comment=request.POST.get('comment')
        comment.save()
        return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(blog=first_post).order_by('-created_at').select_related('user')
    comment_count=comments.count()
    context={"first_post":first_post,
             "comments":comments,
             "comment_count":comment_count}
    return render(request,'blog.html',context)


# search functionality for title,body short description,author,category and comments
def search(request):
    keyword = request.GET.get('keyword')
    blogs = None
    if keyword:
        blogs= Blog.objects.filter(
            Q(title__icontains=keyword) | 
            Q(blog_body__icontains=keyword) | 
            Q(short_description__icontains=keyword) |
            Q(author__username__icontains=keyword) |      
            Q(category__category_name__icontains=keyword)|
            Q(comment__comment__icontains=keyword),
            status='Published').distinct() 
    context = {
        "blogs": blogs,
        "keyword": keyword, 
    }
    return render(request, 'search.html', context)