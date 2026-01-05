from django.contrib import admin
from .models import Category,Blog,Comment
# Register your models here.

admin.site.register(Category)
'''Blog admin customization'''
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=('title','category','author','is_featured','status',)
    # here category is a foreign key 
    search_fields=('id','title','category__category_name','status',)
    list_editable=('is_featured',)
    
'''comment admin customization'''
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('user','blog',)
