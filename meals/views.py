from django.shortcuts import render
from .models import Meal, MealCategory, Department
from .serializers import MealSerializer, MealCategorySerializer, DepartmentSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

class MealList(generics.ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MealDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

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


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class MealCategoryList(generics.ListCreateAPIView):
    queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        

class MealCategoryDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = MealCategory.objects.all()
    serializer_class = MealCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class MealCategoriesByDepartment(generics.RetrieveAPIView):


    model = Department
    queryset = Department.objects.all()
    lookup_field = "pk"


    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        categories = MealCategory.objects.filter(department = instance.id)
        serializer = MealCategorySerializer(categories, many = True)
        return Response(serializer.data)


