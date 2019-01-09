from django.contrib import admin

# Register your models here.

from . import models
from  login.models import User
from album.models import Album
class AlbumInline(admin.StackedInline):
    model = Album


    




admin.site.register(models.ConfirmString)
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'sex', 'c_time', 'has_confirmed')

    list_per_page = 50

    ordering = ('-id',)

    list_editable = ['has_confirmed']

    inlines = [AlbumInline, ]