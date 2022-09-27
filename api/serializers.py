from pyexpat import model
from wsgiref.validate import validator
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password



#serializer to user details 
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields =["id", "first_name", "last_name","username"]
        
        
#serializer to register user

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True,
    validators = [UniqueValidator(queryset = User.objects.all())])
    password = serializers.CharField(write_only =True, required = True,)
    password2 = serializers.CharField(write_only = True, required = True)
    class Meta:
        model = User 
        fields = ('username', 'password', 'password2', 'email', 'first_name','last_name')
        extra_kwargs= {
            'first_name':{'required':True},
            'last_name':{'required':True},
            
        }
        def create(self, validated_data):
            if validated_data.post('password') != validated_data.get('confirm_password'):
                raise serializers.ValidationError("Those password don't match") 

            elif validated_data.post('password') == validated_data.get('confirm_password'):
                       validated_data['password'] (
                validated_data.post('password'))
            
        def create(self, validated_data):
            user = User.objects.create(
                username = validated_data['username'],
                email = validated_data['email'],
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name']
                   
            )
            validated_data.pop('confirm_password') # add this
            return super(RegisterSerializer, self).create(validated_data)