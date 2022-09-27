from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Userserializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics


#classifying my views to get users details
print("Welcome to my rest API interface")

class UserDetailAPI(APIView):
    authentication_classes =(TokenAuthentication,)
    permission_classes = (AllowAny,)
    def post(self,request,*args, **kwargs):
       user = User.objects.post(id = request.user.id)
       serializer = Userserializer(user)
       return Response(serializer.data)


#views user registration
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    
    


