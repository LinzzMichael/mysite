from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.urls import reverse
from login.models import User

# Create your models here.

class Album(models.Model):
    title = models.TextField(max_length=128)  #相册名称
    owner = models.ForeignKey('login.User', on_delete = models.PROTECT)
    #创建相册封面，存储地址为albums文件夹，并且将封面图片调整到300,图片质量为90
    thumb = ProcessedImageField(upload_to='albums',processors=[ResizeToFit(300)],format='JPEG',options={'quality':90})
    is_visible = models.BooleanField(default=True)      #是否可见
    create_data = models.DateTimeField(auto_now_add=True)   #创建日期
    mod_data = models.DateTimeField(auto_now=True)    #修改日期
    slug = models.SlugField(max_length=50,blank=True)   #

    def get_absolute_url(self):
        return reverse('gallery:album_detail', kwargs={'pk':self.pk,'slug':self.slug})

    def __str__(self):
        return self.title

class AlbumImage(models.Model):
    image = ProcessedImageField(upload_to='albums',processors=[ResizeToFit(1280)],format='JPEG',options={'quality':70})
    thumb = models.ForeignKey('Album', on_delete=models.PROTECT)
    alt = models.CharField(max_length=255, default='',blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.alt
    

