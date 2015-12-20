from django.db import models
from django.contrib.auth.models import User
import datetime

DEFAULT_VALUE=1

class QuestionsManager(models.Model):
	def newest(self):
		return self.order_by('-id')

	def hot(self):
		return self.order_by('-rating')


class Question(models.Model):
	user = models.ForeignKey(User, default=DEFAULT_VALUE)
	title = models.CharField(default='', max_length = 255)
	text = models.TextField(default='')
	rating = models.IntegerField(default=0, db_index=True)
	created = models.DateTimeField(default=datetime.datetime.now)
	objects = QuestionsManager()
	def __unicode__(self):
		return self.title

class Answer(models.Model):
	user = models.ForeignKey(User, default=DEFAULT_VALUE)
	question = models.ForeignKey(Question)
	text = models.TextField(default='')
	rating = models.IntegerField(default=0)

	def __unicode__(self):
		return self.text
