from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	content = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	completion_date = models.DateField()

	def __str__(self):
		return self.title

class Skill(models.Model):
	name = models.CharField(max_length=200)
	rating = models.IntegerField()

	def __str__(self):
		return self.name

class Experience(models.Model):
	title = models.CharField(max_length=200)
	employer = models.CharField(max_length=200)
	start_date = models.DateField()
	end_date = models.DateField()
	description = models.TextField()

	def __str__(self):
		return self.title