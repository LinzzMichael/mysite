from django.urls import path,re_path
from . import views

app_name = 'login'


#使用re_path可以在url中加入正则表达式
urlpatterns = [
    path('index/', views.index),
    path('login/', views.login,name="login"),
    path('register/', views.register,name="register"),
    path('logout/', views.logout,name="logout"),
    path('confirm/', views.user_confirm),
    path('', views.login),
]