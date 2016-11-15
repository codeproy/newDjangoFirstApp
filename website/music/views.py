#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from django.http import Http404
from .models import Album

def index(request):
    all_albums = Album.objects.all()
#    template = loader.get_template('music/index.html')
 #   context = {'all_albums' : all_albums,}
#    return HttpResponse(template.render(context,request))
    return render(request,'music/index.html',{'all_albums' : all_albums})

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album Does Not Exist")
    return render(request, 'music/detail.html', {'Album': album })
