"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
# import login.views
# import album.views
from django.views.static import serve
# 自己项目下的settings文件内的MEDIA_ROOT属性
from mysite.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('album/',include('album.urls')),
    # path('index/', login.views.index),
    # path('login/', login.views.login),
    # path('register/', login.views.register),
    # path('logout/', login.views.logout),
    path('captcha/', include('captcha.urls')),
    # path('confirm/', login.views.user_confirm),
    # path('photo/', album.views.myAlbum),
    # path('upload/',album.views.myAlbum),
    # path('media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    path('',include('login.urls')),
]
