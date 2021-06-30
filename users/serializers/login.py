""" User login serializer """

#Django
from django.contrib.auth import authenticate

#Django REST framework
from rest_framework import serializers


class UserLoginSerializer (serializers.Serializer):
    """ Handle the login request data """

    username = serializers.CharField(max_length=150)
    password = serializers.CharField(min_length=8, max_length=128)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])

        if not user:
            return serializers.ValidationError('Invalid credentials')
        
        return data
