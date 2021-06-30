""" Signup a user serializer """

#Django
from django.contrib.auth import password_validation

#Django REST framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#Models
from django.contrib.auth.models import User
from users.models import Profile


class UsersSignupSerializer(serializers.Serializer):
    """ Handle Sign in data validation and user/profile creation """
    username = serializers.CharField(min_length=4,
                                    max_length=150,
                                    allow_blank=False,
                                    validators=[UniqueValidator(queryset=User.objects.all())])
    
    email = serializers.CharField(max_length=150,
                                    allow_blank=False,
                                    validators=[UniqueValidator(queryset=User.objects.all())])
    
    password = serializers.CharField(min_length=8, max_length=128, allow_blank=False)
    password_confirmation = serializers.CharField(min_length=8, max_length=128, allow_blank=False)

    first_name = serializers.CharField(max_length=150, allow_blank=False)
    last_name = serializers.CharField(max_length=150, allow_blank=False)
    
    city = serializers.CharField(max_length=100, allow_blank=False)
    country = serializers.CharField(max_length=100, allow_blank=False)
    likes = serializers.CharField()
    followers = serializers.CharField()
    posts = serializers.CharField()

    def validate(self, data):
        pass

    def create(self, data):
        pass