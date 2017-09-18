from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext,loader
# Create your views here.

from fetcher import fetcher
ft = fetcher()
def index(request):
	urllist = ft.GetPhotosFromFlickr()
	Url_context = {"urllist":urllist}
	context=RequestContext(request)
	
    	return render_to_response("photo.html",Url_context,context)
