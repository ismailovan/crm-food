from django.urls import path

from .views import *

app_name = 'meals'
urlpatterns = [
    path('meal-categories/', MealCategoryList.as_view()),
    path('meal-categories/<int:pk>/', MealCategoryDetail.as_view()),
    path('departments/', DepartmentList.as_view()),
    path('departments/<int:pk>/', DepartmentDetail.as_view()),
    path('meals/', DepartmentList.as_view()),
    path('meals/<int:pk>/', DepartmentDetail.as_view()),
    path('meal-categories-by-department/<int:pk>/', MealCategoriesByDepartment.as_view()),

    
]
