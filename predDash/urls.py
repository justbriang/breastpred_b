from django.contrib import admin
from django.urls import path,include
from .views import home,addUtils,loginPage,registerPage,logoutUser

urlpatterns = [
    path('', home,name='home'),
    path('login', loginPage, name="login"),
    path('register',registerPage, name="register"),
    path('logout', logoutUser, name="logout"),
    path('/addUtils', addUtils,name='addUtils'),
   
]
