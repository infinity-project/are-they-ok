from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from stream_django.activity import Activity

# Create your models here.


class Update(models.Model, Activity):
	created_at = models.DateTimeField(auto_now_add=True)
	client = models.ForeignKey(User, default='Boundarybreaker')
	
	@property
	def activity_actor_attr(self):
		return self.client