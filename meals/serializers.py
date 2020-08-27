from .models import Department, MealCategory, Meal
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Department
		fields = ('id', 'name')

class MealCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = MealCategory
		fields = ('id', 'name', 'department')

class MealSerializer(serializers.ModelSerializer):
	class Meta:
		model = Meal
		fields = ('id', 'name', 'category', 'price', 'description')

