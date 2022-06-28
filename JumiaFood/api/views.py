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
        total_amount = 0
        
        for i in data['item']:
            menu_query = Menu.objects.get(pk=i["menu"])
            menu_price = menu_query.price
            
            Price = i["quantity"] * menu_price
            total_amount += Price
        
        serializer = self.serializer_class(data=data)

        user = request.user

        if serializer.is_valid():
            serializer.save(customer=user,total_amount=total_amount)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)


class OrderUpdateApiView(generics.UpdateAPIView):
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'


    def update(self, request,*args,**kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data,partial= True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"order has been updated"})

        else:
            return Response({"message":"order did not update"})

class OrderRetrieveApiView(generics.RetrieveAPIView):
    
    queryset = Order.objects.all()
    serializer_class = OrderRetrieveSerializer
    lookup_field = 'pk'

class OrderDeleteApiView(generics.DestroyAPIView):
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'


    