from django.db import models

# Create your models here.

class Department(models.Model):
	name = models.CharField(max_length = 255)
	def __str__(self):
		return self.name

class MealCategory(models.Model):
	name =  models.CharField(max_length = 255)
	department = models.ForeignKey(Department,on_delete =  models.CASCADE)
	def __str__(self):
		return self.name

class Meal(models.Model):
	name = models.CharField(max_length = 255)
	category = models.ForeignKey(MealCategory,on_delete =  models.CASCADE)
	price = models.IntegerField(max_length = 255)
	description = models.CharField(max_length = 255)
	def __str__(self):
		return self.name

