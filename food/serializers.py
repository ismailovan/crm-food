from rest_framework import serializers
from .models import *

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

class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = ('id', 'name')

class ServicePercentageSerializer(serializers.ModelSerializer):
	class Meta:
		model = ServicePercentage
		fields = ('percentage', )
	
class TableSerializer(serializers.ModelSerializer):
	class Meta:
		model = Table
		fields = ('id', 'name')

class MealToOrderSerializer(serializers.ModelSerializer):
    meal = serializers.CharField()
    count = serializers.IntegerField()
    amount = serializers.IntegerField(read_only=True, source='get_sum')


    class Meta:
        model = MealToOrder
        fields = ('id', 'meal', 'count',  'amount')



class OrderSerializer(serializers.ModelSerializer):
    
    meal_id = MealToOrderSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ('id', "table", "waiter", "date", "is_open", "meal_id")
    def create(self, validated_data):
        meals = validated_data.pop('meal_id')
        order = Order.objects.create(**validated_data)
        for meals in meals:
            MealToOrder.objects.create(**meals, order=order)
        return order

class CheckSerializer(serializers.ModelSerializer):
    meal = MealToOrderSerializer(read_only=True)
    servicefee = ServicePercentageSerializer(read_only=True)
    total_sum = serializers.IntegerField(source='get_total_sum', read_only=True)

    class Meta:
        model = Check
        fields = ('id', 'order', 'date', 'servicefee', 'total_sum', 'meal')
