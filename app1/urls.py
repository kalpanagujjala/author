from django.urls import path
from app1 import views

urlpatterns=[
    path('',views.home,name='home'),
    path('create',views.createauthor,name='author'),
    path('book',views.createbook,name='book'),
]