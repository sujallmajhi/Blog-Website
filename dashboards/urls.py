from django.urls import path
from .import views
urlpatterns=[
  # dashboard
    path('',views.dashboard,name="dashboard"),
    #categories management urls
    path('categories/',views.category,name='categories'),
    path('categories/add/',views.add_category,name='add_category'),
    path('categories/edit/<int:pk>/',views.edit_category,name='edit_category'),
     path('categories/delete/<int:pk>/',views.delete_category,name='delete_category'),
     # post management urls
     path('posts/',views.posts,name='posts'),
     path('post/add/',views.add_posts,name="add_posts"),
       path('post/edit/<int:pk>/',views.edit_posts,name="edit_posts"),
        path('post/delete/<int:pk>/',views.delete_posts,name="delete_posts"),
        #users management urls
        path('users/',views.users,name='users'),
        path('users/add/',views.add_user,name='add_user'),
        path('users/edit/<int:pk>/',views.edit_user,name='edit_user'),
        path('users/delete/<int:pk>/',views.delete_user,name='delete_user'),
]

