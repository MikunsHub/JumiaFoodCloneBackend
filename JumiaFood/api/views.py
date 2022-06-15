from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response

from .models import  *
from .serializers import  *

class CountryCreateListApiView(generics.ListCreateAPIView):

    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    # print(queryset)

    def get(self,request):
        
        countries = Country.objects.all()
        serializer = self.serializer_class(instance=countries,many=True)
        return Response(data=serializer.data)

    def post(self,request):
        serializer = CountrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class Business_TypeCreateListApiView(generics.ListCreateAPIView):
    serializer_class = Business_TypeSerializer
    queryset = Business_Type.objects.all()
    # print(queryset)

    def get(self,request):
        
        business_type = Business_Type.objects.all()
        serializer = self.serializer_class(instance=business_type,many=True)
        return Response(data=serializer.data)

class VendorCreateListApiView(generics.ListCreateAPIView):

    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()

    def get(self,request):
        
        vendor = Vendor.objects.all()
        serializer = self.serializer_class(instance=vendor,many=True)
        return Response(data=serializer.data)

    def post(self,request):
        serializer = VendorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class MenuCreateListApiView(generics.ListCreateAPIView):

    serializer_class = MenuSerializer
    queryset = Menu.objects.all()

    def get(self,request):
        
        vendor = Menu.objects.all()
        serializer = self.serializer_class(instance=vendor,many=True)
        return Response(data=serializer.data)

    def post(self,request):
        serializer = MenuSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class OrderCreateListApiView(generics.ListCreateAPIView):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get(self,request):
        
        order = Order.objects.all()
        serializer = self.serializer_class(instance=order,many=True)
        return Response(data=serializer.data)

    def post(self,request):

        data = request.data
        print(data)
        # {'status': 'pending', 'items': [1, 2]}
        

        serializer = self.serializer_class(data=data)

        user = request.user



        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)