from __future__ import absolute_import
from django.conf.urls import *
from . import views

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),			
	url(r'^add/$', views.add_game, name = 'add-game'),
	url(r'^edit/(?P<game_guid>\w+)/$', views.edit_game, name = 'edit-game' ),
	url(r'^delete/(?P<game_guid>\w+)/$', views.delete_game, name = 'delete-game'),
	
	url(r'^(?P<username>\w+)/(?P<game_guid>\w+)/$', views.game_detail, name='game_detail'),
	url(r'^(?P<username>\w+)/$', views.user_detail, name='user_detail'),
)
