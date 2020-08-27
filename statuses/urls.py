from django.urls import path

from .views import *

app_name = 'statuses'
urlpatterns = [
    path('statuses/', StatusList.as_view()),
    path('statuses/<int:pk>/', StatusDetail.as_view()),
    path('service-percentage/', ServicePercentageList.as_view()),
    path('service-percentage/<int:pk>/', ServicePercentageDetail.as_view()),
]
