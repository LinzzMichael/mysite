from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Album,AlbumImage
from django.shortcuts import redirect
import login
import uuid 
import os

# Create your views here.

def photo(request):
	pass
	return render(request, 'album/index.html')



# class AlbumListView(ListView):
# 	queryset = Album.objects.filter(is_visible=True).order_by('-create_date')
# 	paginate_by = 1


# class AlbumDetail(DetailView):
# 	model = Album
# 	def get_context_data(self,**kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['images'] = AlbumImage.objects.filter(album=self.object.id)

# 		return context


def uploadImg(request):
	if request.method == 'POST':
		if  request.session.get('is_login', None):
			ownerName = request.session.get('user_name', None)
			owner = login.models.User.objects.get(name=ownerName)
			newImage = Album(title="uplpadTest",
						owner = owner,
						thumb = request.FILES.get('img')
			)
			newImage.save()
		else:
			return redirect('/login/')
	content = []
	return render(request, 'album/upload.html')


def createAlbum(request):
	if request.method == 'POST':
		if request.session.get('is_login', None):
			ownerName = request.session.get('user_name', None)
			owner = login.models.User.objects.get(name=ownerName)
			title = request.POST['title']
			introduction = request.POST['introduction']
			is_visible = request.POST['public']
			newAlbum = Album(title = title,
						owner = owner,
						thumb = request.FILES.get('img'),
						introduction = introduction,
						is_visible = is_visible
			 )
			# file = request.FILES.get('img')
			# ext = file.name.split('.')[-1]
			# filename = '{}.{}'.format(uuid.uuid4(),ext)
			# path = os.path.join("media", str(owner.id), "albums",filename)
			newAlbum.save()
			return redirect('/album/')
		else:
			return render(request, 'album/myAlbum.html')
	return render(request, 'album/myAlbum.html') 


def myAlbum(request):
	if request.method == 'GET':
		if request.session.get('is_login', None):
			ownerName = request.session.get('user_name', None)
			owner = login.models.User.objects.get(name=ownerName)
			albums = Album.objects.filter(owner=owner) 
			return render(request, 'album/myAlbum.html',locals())

	return render(request, 'album/myAlbum.html')



# #获取上传文件的保存路径的函数,此处仅获取对应用户的文件夹
# #后续路径由处理函数处理
# def getUploadPath(user):
# 	user_uuid = uuid.uuid4.hex[:10]
# 	return user_uuid