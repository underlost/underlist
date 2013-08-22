import datetime

from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

GENDER_CHOICES = (
	('F', _('Female')),
	('M', _('Male')),
	('P', _('Pirate')),
	('N', _('Ninja')),
	('R', _('Robot')),
)


class Profile(AbstractUser):
	gender			  = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
	location 		  = models.CharField(max_length=255, blank=True)
	url				  = models.URLField(max_length=500, blank=True)
	about			  = models.TextField(max_length=500, blank=True)
	
	#Settings
	hide_mobile       = models.BooleanField(default=False)
	last_seen_on      = models.DateTimeField(default=datetime.datetime.now)
	preferences       = models.TextField(default="{}")
	view_settings     = models.TextField(default="{}")
	send_emails       = models.BooleanField(default=False)
	is_beta			  = models.BooleanField(default=False)
	