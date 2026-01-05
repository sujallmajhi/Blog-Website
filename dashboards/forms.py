from django import forms
from blogs.models import Category,Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# category form,where all fields of category model are included
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

#blog post form where all fields of blog models are included where authhor field is excluded as it will be set in views using request.user
class BlogPostForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('title','category','featured_image','short_description','blog_body','status','is_featured',)


# user management forms
class AddUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions',)
# Edit user forms 
class EditUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions',)
