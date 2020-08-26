from django.shortcuts import render
from .models import Meal, MealCategory, Department
from .serializers import MealSerializer, MealCategorySerializer, DepartmentSerializer
from rest_framework import status
from rest_framework import generics

class MealList(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MealDetail(generics.ListCreateAPIView):
	queryset = Meal.objects.all()
    serializer_class = MealSerializer

	def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
    	return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DepartmentDetail(generics.ListCreateAPIView):
	queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

	def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class MealCategoryList(generics.ListCreateAPIView):
	queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MealCategoryDetail(generics.ListCreateAPIView):
	queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


