from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='blog_list'),
    path('Blogs/', articles ),
    path('Blogs/post/<int:pk>/',blog_expand),
    path('about/',about_page),
]