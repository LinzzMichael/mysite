from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Album,AlbumImage
from django.shortcuts import redirect
import login

# Create your views here.

def photo(request):
	pass
	return render(request, 'photoshow/portfolio.html')



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
	return render(request, 'photoshow/upload.html')

		
	