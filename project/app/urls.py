
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('dashboard/',views.dashboard,name="dashboard"),
    # path('first/',views.first,name="first"),
    # path('last/',views.last,name="last"),
    # path('latest/',views.latest,name="latest"),
    # path('earliest/',views.earliest,name="earliest"),
    # path('exists/',views.exists,name="exists"),
#     path('all_details/',views.all_details,name="all_details"),
#     path('filter/',views.filter,name="filter"),
#     path('exclude/',views.exclude,name="exclude"),
#     path('ascending/',views.acending,name="ascending"),
#     path('descending/',views.descending,name="descending"),
#     path('random/',views.random,name="random"),
#     path('slice/',views.slice,name="slice"),
    path('query/',views.query,name="query"),
    path('edit/<int:x>',views.edit,name="edit"),
    path('delete/<int:x>',views.delete,name="delete"),
    path('update/<int:x>',views.update,name="update")
 ]