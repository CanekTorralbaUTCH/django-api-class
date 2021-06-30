#Django REST framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

#Models
from django.contrib.auth.models import User
from users.models import Profile

#Serializer
from users.serializers.users import UserSerializer
from users.serializers.signup import UsersSignupSerializer

@api_view(['GET'])
def users(request):
    if request.method == 'GET':
        users = User.objects.filter(is_staff=False)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def signup(request):

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        data = UserSerializer(user).data
        return Response(data)
