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


	
class TableSerializer(serializers.ModelSerializer):
	class Meta:
		model = Table
		fields = ('id', 'name')

class MealToOrderSerializer(serializers.ModelSerializer):

    meal_id = serializers.PrimaryKeyRelatedField(
        queryset=Meal.objects.all()
    )

    name = serializers.CharField(source='meal_id.name', read_only=True)

    class Meta:
        model = MealToOrder
        fields = ("meal_id", "count", "name",)



class OrderSerializer(serializers.ModelSerializer):
    
    table_id = serializers.PrimaryKeyRelatedField(
        queryset=Table.objects.all()
    )
    table_name = serializers.SerializerMethodField("get_table_name")
    is_open = serializers.SerializerMethodField("get_is_open")
    meals = MealToOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = (
                "id",
                "waiter",
                "table_id",
                "table_name",
                "is_open",
                "date",
                "meals",
        )
        read_only_fields = ("id", "is_open", "waiter")

    def get_is_open(self, obj):
        is_open = obj

        if is_open:
            return 1
        else:
            return 0

    def get_table_name(self, obj):
        table = obj.table_id

        return str(table)

    def create(self, validated_data):
       
        meals = validated_data.pop("meals")
        order = Order.objects.create(**validated_data)

        for menu_meal in meals:
            MealToOrder.objects.create(order=order, **menu_meal)

        return order
class ServicePercentageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePercentage
        fields = ('percentage', )

class CheckSerializer(serializers.ModelSerializer):
    meals = MealToOrderSerializer(many=True, source='order.meals', read_only=True)

    servicefee = serializers.PrimaryKeyRelatedField(
        queryset=ServicePercentage.objects.all()
    )

    total = serializers.FloatField(source='get_sum', read_only=True)
    class Meta:
        model = Check
        fields = ('id', 'order', 'date', 'servicefee', 'total', 'meals')
        read_only_fields = ( "date", "servicefee", 'menu_meal')
