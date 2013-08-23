import datetime
import markdown

from django.conf import settings
from django.db import models
from django.contrib.sites.models import Site
from django.utils.encoding import smart_unicode, smart_str
from django.utils.translation import ugettext_lazy as _

#from django.contrib.auth.models import User
from underlist.core.models import Profile as User

class GameManager(models.Manager):
		
	def completed(self):
		return super(GameManager, self).get_query_set().filter(status=3)

	def played(self):
		Return super(GameManager, self).get_query_set().filter(status=[2,3,4])

STATUS_CHOICES = (
	(1, u'Unplayed'),
	(2, u'Playing'),
	(3, u'Completed'),	
	(4, u'Given Up'),
)
	
class Game(models.Model):
	game = models.TextField(max_length=255)
	user = models.ForeignKey(User, related_name="my_games")
	added = models.DateTimeField(verbose_name=_("Date added"), help_text=_("Time game was added to the list"), default=datetime.datetime.now)
	date_completed = models.DateTimeField(verbose_name=_("Completed date"), help_text=_("Date game was completed"), blank=True, null=True)
	is_owned = models.BooleanField(help_text=_("Should be checked if you own a copy."), default=True)
	status = models.IntegerField(choices=STATUS_CHOICES, max_length=1)
	note = models.TextField(blank=True)
	note_html = models.TextField(blank=True)

	objects = GameManager()
	
	def __unicode__(self):
		return self.game

	class Meta:
		db_table = 'backlog_games'
		verbose_name_plural = 'games'
		ordering = ('-added',)
		get_latest_by = 'added'


	def save(self, *args, **kwargs):   
		self.note_html = markdown.markdown(smart_unicode(self.note))
		super(Game, self).save(*args, **kwargs)        