# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="JGalex"
__date__ ="$10/11/2013 04:21:02 PM$"

from django.conf.urls import patterns, url
from posts import views

urlpatterns = patterns('',
						url(r'^(?P<posterId>\w+)/(?P<valor>)$',views.RatingView,name='rating'),
						url(r'^(?P<rate>\w+)/(?P<id_Publicacion>)$', views.set_rate),
						)