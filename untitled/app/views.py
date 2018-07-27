from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import *


# Create your views here.

def artistdetails(request, name):
    output = '<html><head><title>' + name
    output += '</title></head><body><h1>' + name
    output += '</h1></body></html>'
    return HttpResponse(output)


def artistid(request, pk_id):
    artist = Artist.objects.get(pk=pk_id)
    return render_to_response("artistdetails.html", {"artists": artist})  # artists.html取于templates文件夹下


# def home(request):
#     """Randers the home page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         "app/index.html",
#         context_instance=RequestContext(request, {
#             "title": "Home Page",
#             "year": datetime.now().year,
#         })
#     )


def artists(request):
    # return HttpResponse('<html><head><title>Hello, Django!</title></head><body><h1>Hello, Django</h1></body></html>')
    artist = Artist.objects.all()
    return render_to_response("artists.html", {"artists": artist})  # artists.html取于templates文件夹下


def artistcreate(request):
    if request.method == "GET":
        form = ArtistForm()
        return render(request, "create.html", {"form": form})
    elif request.method == "POST":
        form = ArtistForm(request.POST)
        form.save()
        return HttpResponseRedirect("/artists")
