from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework import serializers, generics
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)

@api_view()
def user_apiview(request):
    user = User.objects.first()
    data = UserSerializer(user).data
    return Response(data)

class UserList(generics.ListAPIView):
	queryset = User.objects.all()		
	serializer_class = UserSerializer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/1/', user_apiview),
    path('api/users/', UserList.as_view()),
]
