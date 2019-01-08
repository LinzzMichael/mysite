from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Album,AlbumImage
from django.shortcuts import redirect
import login

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

	