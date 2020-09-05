from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.

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

class StatusList(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        

class StatusDetail(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ServicePercentageList(generics.ListCreateAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        

class ServicePercentageDetail(generics.ListCreateAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class TableList(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TableDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_active_orders(self, *args, **kwargs):
        return Order.objects.filter(is_open=True)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderMeal(generics.ListCreateAPIView):
    model = MealToOrder
    serializer_class = MealToOrderSerializer
    permission_classes = (IsAuthenticated,)
    queryset = MealToOrder.objects.all()

class CheckList(generics.ListCreateAPIView):
    model = Check
    serializer_class = CheckSerializer
    queryset = Check.objects.all()

class CheckDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Check
    serializer_class = CheckSerializer
    queryset = Check.objects.all()