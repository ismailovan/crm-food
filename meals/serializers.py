from .modeld import Department, MealCategory, Meal
from rest_framework import serializers


class DepartmentSerializer(models.Model):
	class Meta:
		model = Department
		fields = ('name')

class MealCategorySerializer(models.Model):
	class Meta:
		model = MealCategory
		fields = ('name', 'department_id')

class MealSerializer(models.Model):
	class Meta:
		model = Meal
		fields = ('name', 'category_id', 'price', 'description')

