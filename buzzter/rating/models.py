# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="JGalex"
__date__ ="$10/11/2013 04:30:44 PM$"

from django.db import models
from pofiles.models import Profile
from posts.models import Post

class Rating(models.Model):
	'''
	Esta clase representa el valor con el que un usuario
	calificara una publicación hecha

	__date__ 10/11/2013 16:41
	__author__ Jorge
	branch: JGBranch
	'''
	
	usuario = models.ForeignKey(Profile, related_name="posts")
	rate = models.PositiveIntegerField(blank=True, null=True, default=0)
	publicacion = model.ForeignKey(Post, related_name=)