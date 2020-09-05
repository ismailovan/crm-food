from django.db import models
from users.models import User

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

class ServicePercentage(models.Model):
	percentage =  models.IntegerField(max_length = 255)

	
class Table(models.Model):
	name =  models.CharField(max_length = 255)
	def __str__(self):
		return self.name

class Order(models.Model):
    waiter = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Waiter')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name='Table')
    is_open = models.BooleanField(default = True)
    date = models.DateField(auto_now_add=True)

    def get_total_sum(self):
        return sum(meal.get_sum() for meal in self.meal_id.all())

    def __str__(self):
        return '{}, {}'.format(self.waiter, self.table)


class MealToOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='meal_id')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(verbose_name='Count')

    def get_sum(self):
        return self.count * self.meal.price

class Check(models.Model):
    order = models.ForeignKey(Order, related_name="order_id", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    servicefee = models.ForeignKey(ServicePercentage, related_name="servicefee", on_delete=models.CASCADE)

    def get_sum(self):
        return self.order_id.get_total_sum() + self.servicefee.percentage