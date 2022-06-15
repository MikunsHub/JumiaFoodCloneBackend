from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response

from .models import User
from .serializers import  UserSerializer

class RegisterView(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated)
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
