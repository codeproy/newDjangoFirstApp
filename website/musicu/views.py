#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render,get_object_or_404
#from django.http import Http404
from music.models import Album

def index(request):
    all_albums = Album.objects.all()
#    template = loader.get_template('music/index.html')
 #   context = {'all_albums' : all_albums,}
#    return HttpResponse(template.render(context,request))
    return render(request,'musicu/index.html',{'all_albums' : all_albums})

def detail(request, album_x):
 #   try:
 #       album = Album.objects.get(pk=album_id)
 #   except Album.DoesNotExist:
 #       raise Http404("Album Does Not Exist")
    album = get_object_or_404(Album,pk=album_x)
    return render(request, 'musicu/detail.html', {'Album': album })

def favorite(request, album_id):

    album = get_object_or_404(Album,pk=album_id)

    try:
        selected_song = album.song_set.get(id=request.POST['song'])
    except (KeyError,selected_song .DoesNotExist):
        return render(request, 'musicu/detail.html', {'Album': album , 'error_message': 'You did not selected ' })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'musicu/detail.html', {'Album': album })
