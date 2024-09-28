
from django.urls import path,include
from app import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login")
]