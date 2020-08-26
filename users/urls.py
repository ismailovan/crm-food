from django.urls import path

from .views import *

app_name = 'users'
urlpatterns = [
    path('users/reg', RegistrationAPIView.as_view()),
    
    path('users/login/', LoginAPIView.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]
