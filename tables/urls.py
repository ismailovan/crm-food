from django.urls import path

from .views import *

app_name = 'tables'
urlpatterns = [
    path('tables/', TableList.as_view()),
    path('tables/<int:pk>/', TableDetail.as_view()),
]
