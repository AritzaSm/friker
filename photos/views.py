# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import HttpResponse
from photos.models import Photo, PUBLIC
from django.http import HttpResponseNotFound

def home(request):

	photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')

	context = {
		'photo_list': photos[:5]
	}
	

	return render(request, 'photos/home.html', context)

def detail(request,pk):
	""" 
	Carga la página de detalle de la fotos
	:param request: HttpRequest
	:param pk: id de la fotos
	:return: HttpResponse

	"""

	possible_photos = Photo.objects.filter(pk=pk)
	photo = possible_photos[0] if len(possible_photos) == 1 else None

	if photo is not None:
		# Cargamos la Plantilla
		context = {
			'photo' : photo
		}
		return render(request, 'photos/detail.html', context)
	else:
		return HttpResponseNotFound('No Existe la foto') #Mandamos un 404




