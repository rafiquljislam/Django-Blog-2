from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home,name="home"),
    path('contact/', views.contact,name="contact"),
    path('search/', views.search,name="search"),
    path('<str:slug>', views.blogpost,name="blogpost"),
    path('singup/', views.singup1,name="singup"),
    path('loginnow/', views.loginnow,name="loginnow"),
    path('logoutnow/', views.logoutnow,name="logoutnow"),
]
