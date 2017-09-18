import sys
import urllib
from flickrapi import FlickrAPI
import flickrapi
flickr=flickrapi.FlickrAPI("415a65cd75c7ebb42a6d710845add83d","5ea01aea1abe6ead",format='parsed-json')

class fetcher():
	def __init__(self):
		pass
	def GetPhotosFromFlickr(self):

        	ListOfUrls=[]
        	ToGetPhoto = flickr.photos.search(tags="bangalore",extras="url_m",per_pages=5)
        	photos = ToGetPhoto["photos"]
        	PhotoList = photos['photo']
        	for i in PhotoList:
            
            		ListOfUrls.append(i['url_m'])
        	
        	return (ListOfUrls)
            
