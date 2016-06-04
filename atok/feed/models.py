from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
class Update(models.Model):
	update_text = models.CharField(max_length=10)
	user = models.ForeignKey(User)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.update_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		
class Verify(models.Model):
	update = models.ForeignKey(Update, on_delete=models.CASCADE)
	level = models.CharField(max_length=10)
	affirmations = models.IntegerField(default=0)
	def __str__(self):
		return self.level