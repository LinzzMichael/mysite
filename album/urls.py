from django.urls import path,re_path
from . import views

app_name = 'album'


#使用re_path可以在url中加入正则表达式
urlpatterns = [
    # re_path(r'^album/$',views.AlbumListView.as_view(),name='album_list'),
    # re_path(r'^album/(?P\d+)/(?P[-\w]+)/$',views.AlbumDetail.as_view(),name='album_detail'),
    path('', views.myAlbum),
    path('photo/',views.myAlbum)
]