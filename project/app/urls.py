
from django.urls import path,include
from app import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('dashboard/',views.dashboard,name="dashboard"),
    # path('first/',views.first,name="first"),
    # path('last/',views.last,name="last"),
    # path('latest/',views.latest,name="latest"),
    # path('earliest/',views.earliest,name="earliest"),
    # path('exists/',views.exists,name="exists"),
    path('all_details/',views.all_details,name="all_details"),
    path('filter/',views.filter,name="filter"),
]