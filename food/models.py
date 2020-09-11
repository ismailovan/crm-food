from django.db import models
from users.models import User
from django.utils import timezone
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

class Status(models.Model):
	name =  models.CharField(max_length = 255)
	def __str__(self):
		return self.name


	
class Table(models.Model):
    name =  models.CharField(max_length = 255)
    def __str__(self):
        return self.name


class Order(models.Model):
    waiter = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Waiter')
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name='Table')
    is_open = models.BooleanField(default = True)
    date = models.DateField(auto_now_add=True)



    def __str__(self):
        return '{}, {}'.format(self.waiter, self.table_id)

    def add_meals(self, request):
        menu_meal = self.meals

        data = request.data
        meals = data.pop("meals")

        for meal in meals:
            count = meal["count"]
            meal_id = meal["meal_id"]
            try:
                ordered_meal = menu_meal.get(meal_id=meal_id)
                ordered_meal.count += count
                ordered_meal.save()
            except ObjectDoesNotExist:
                md.MealToOrder.objects.create(order=self, count=count, meal_id=meal_id)

        return self



    def delete_meal(self, request):
       
        data = request.data

        menu_meal = self.order_id.get(meal_id=data["meal_id"])
        menu_meal.count -= data["count"]

        if menu_meal.count <= 0:
            menu_meal.delete()
        else:
            menu_meal.save()

        return self

    




class MealToOrder(models.Model):
    meal_id = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='menu_meal')
    count = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name = 'meals')

    def __str__(self):
        return self.name

    def get_price(self):
        return self.meal_id.price * self.count




class ServicePercentage(models.Model):
	percentage =  models.IntegerField(max_length = 255)


class Check(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    servicefee = models.ForeignKey(ServicePercentage, on_delete=models.CASCADE)

    def get_sum(self):
        prices = [meals.get_price() for meals in MealToOrder.objects.filter(order=self.order)]
        summ = sum(prices) + sum(prices) * self.servicefee.percentage
        return summ
