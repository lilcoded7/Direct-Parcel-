from  django.urls import path 
from . import views






urlpatterns = [
    path('', views.home, name='home'),  
    path('register/', views.Register, name='register'),
    path('trackpage/', views.trackitem, name='trackpage'),
    path('registercustomer/', views.customer, name='customer'),
    path('navbar/', views.navbar, name='navbar'),
    path('main/', views.main, name='main')

]

