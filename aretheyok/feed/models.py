from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from stream_django import activity
from django.views.generic.edit import CreateView

# Create your models here.


class Update(activity.Activity, models.Model):
	user = models.ForeignKey('auth.User')
	text = models.CharField(max_length=160)
	created_at = models.DateTimeField(auto_now_add=True)
	
	@property
	def activity_object_attr(self):
		return self
	
class Follow(models.Model):
	user = models.ForeignKey('auth.User', related_name='friends')
	target = models.ForeignKey('auth.User', related_name='followers')
	created_at = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		unique_together = ('user', 'target')