from django.db import models

# Create your models here.
class Status(models.Model):
	name =  models.CharField(max_length = 255)
	def __str__(self):
		return self.name

class ServicePercentage(models.Model):
	percentage =  models.IntegerField(max_length = 255)
	def __str__(self):
		return self.percentage
