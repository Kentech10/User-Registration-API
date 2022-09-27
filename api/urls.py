from django.urls import path,include
from .views import UserDetailAPI,RegisterUserAPIView 




urlpatterns = [
  
    path("get-details",UserDetailAPI.as_view()),
    path('', RegisterUserAPIView.as_view()),
]