from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Update(models.Model):
	update_text = models.CharFiend(max_length=10)
	pub_date = models.DateTimeField('date published')
	
class Verify(models.Model)
	update = models.ForeignKey(Update, on_delete=models.CASCADE)
	level = models.PositiveSmallIntegerField(default=1)
	affirmations = models.IntegerField(default=0)