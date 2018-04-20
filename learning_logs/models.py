from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
	""""""
	title = models.CharField(max_length=200)
	pup_date = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User)

	def __str__(self):
		return self.title


class Entry(models.Model):
	""""""
	topic = models.ForeignKey(Topic)
	text = models.TextField()
	pup_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "entries"

	def __str__(self):
		if len(self.text) < 50:
			return self.text
		else:
			return self.text[:50]