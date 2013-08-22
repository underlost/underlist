from __future__ import absolute_import

import hashlib
import json
import functools
import datetime

from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.core import cache
from django.http import HttpResponse

from .models import Game
from underlist.core.models import Profile as User

from underlist.utils import giantbomb 
gb = giantbomb.Api('a93fd9904abaec420c9a364fa4602b45d45c2358')  

def index(request):
    if request.user.is_authenticated():
    	template = 'backlog/index.html'
    	games = Game.objects.filter(user=request.user)
    	ctx = {
    	    'unplayed' = games.unplayed()
    	    'playing' = games.playing()
    	    'completed' = games.completed()
    	    'givenup' = games.givenup()
    	}

    else:
		template = 'backlog/welcome.html'
		ctx = {}
    return render(request, template, ctx)


def profile(request, username):
   
    u = get_object_or_404(User, username=username)
    games = Game.objects.filter(user=u)
        
    ctx = {
        'user_obj': u,
        'email_hash': hashlib.md5(u.email).hexdigest(),
        'unplayed' = games.unplayed()
        'playing' = games.playing()
        'completed' = games.completed()
        'givenup' = games.givenup()
    }
    return render(request, "backlog/profile.html", ctx)

@login_required
def add_list(request):
	#add a list.
	instance = FeedList(owner=request.user)
	f = FeedListModelForm(request.POST or None, instance=instance)
	if f.is_valid():
		entry = f.save(commit=False)
		entry.owner = request.user
		entry.save()
		f.save_m2m()
		messages.add_message(
			request, messages.INFO, 'New list created.')
		return redirect('index')

	ctx = {'form': f, 'adding': True}
	return render(request, 'aggregator/edit-list.html', ctx) 

@login_required
def edit_list(request, list_guid):
	instance = get_object_or_404(FeedList, guid=list_guid, owner=request.user)
	f = FeedListModelForm(request.POST or None, instance=instance)
	if f.is_valid():
		entry = f.save(commit=False)
		entry.owner = request.user
		entry.save()
		f.save_m2m()
		messages.add_message(
			request, messages.INFO, 'List successfully edited.')
		return redirect('index')

	ctx = {'form': f, 'adding': False}
	return render(request, 'aggregator/edit-list.html', ctx) 

@login_required
def delete_list(request, list_guid):
	list = get_object_or_404(FeedList, guid=list_guid, owner=request.user)
	if request.method == 'POST':
		list.delete()
		return redirect('my-lists')
	return render(request, 'aggregator/delete-confirm-list.html', {'list': list})
