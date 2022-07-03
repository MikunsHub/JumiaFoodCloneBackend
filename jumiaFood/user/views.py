from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response

from .models import User
from .serializers import  UserSerializer, DriverRegisterSerializer

# class RegisterView(generics.ListCreateAPIView):
#     # permission_classes = (IsAuthenticated)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     def post(self,request):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

class RegisterView(generics.GenericAPIView):
    # permission_classes = (IsAuthenticated)
    # queryset = User.objects.all()
    serializer_class = DriverRegisterSerializer
    def post(self,request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        driver = serializer.save()
        driver_data = DriverRegisterSerializer(driver, context=self.get_serializer_context()).data
        return Response(serializer.data)

# def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         individual = serializer.save()
#         individual_data = IndividualSerializer(individual, context=self.get_serializer_context()).data
        
#         return Response({
#              "individual": individual_data,
#              "username": individual.user.username,
#              "token": AuthToken.objects.create(individual.user)[1]
#         })