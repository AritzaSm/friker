# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Tuplas para las licencias
COPYRIGHT='RIG'
COPYLEFT ='LEF'
CREATIVE_COMMONS = 'CC'

LICENSES = (
	(COPYRIGHT,'CopyRigth'),
	(COPYLEFT,'CopyLeft'),
	(CREATIVE_COMMONS,'Creative Commons')
	)

# Tuplas para la visibilidad 
PUBLIC = 'PUB'
PRIVATE = 'PRI'

VISIBILITY = (
	(PUBLIC,'Pública'),
	(PRIVATE, 'Privada')
	)

# Clase para las fotos
class Photo(models.Model):

	name = models.CharField(max_length=150)
	url = models.URLField()
	description = models.TextField(blank=True, null=True, default="")
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)
	license = models.CharField(max_length=3, choices=LICENSES)	
	visibility = models.CharField(max_length=3, choices=VISIBILITY, default=PUBLIC)
	owner = models.ForeignKey(User)
	# Metodo privado, metodo especial. 
	def __unicode__(self): ## en la version 3 es __str__

		return self.name
