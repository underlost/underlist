from django.contrib import admin
from .models import Game
from django.utils.translation import ugettext_lazy as _

class GameAdmin(admin.ModelAdmin):
	list_display = ('game', 'user', 'added')
	list_filter = ('is_played', 'is_owned', 'is_complete')
	
admin.site.register(Game, GameAdmin)
