from django.urls import path

from .views import *

app_name = 'food'
urlpatterns = [
    path('tables/', TableList.as_view()),
    path('tables/<int:pk>/', TableDetail.as_view()),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='retrieve'),
    path('mealToOrder/<int:pk>', OrderMeal.as_view()),
    path('meal-categories/', MealCategoryList.as_view()),
    path('meal-categories/<int:pk>/', MealCategoryDetail.as_view()),
    path('departments/', DepartmentList.as_view()),
    path('departments/<int:pk>/', DepartmentDetail.as_view()),
    path('meals/', MealList.as_view()),
    path('meals/<int:pk>/', MealDetail.as_view()),
    path('meal-categories-by-department/<int:pk>/', MealCategoriesByDepartment.as_view()),
    path('statuses/', StatusList.as_view()),
    path('statuses/<int:pk>/', StatusDetail.as_view()),
    path('service-percentage/', ServicePercentageList.as_view()),
    path('service-percentage/<int:pk>/', ServicePercentageDetail.as_view()),
    path('check/', CheckList.as_view()),
    path('check/<int:pk>', CheckDetail.as_view())
]
