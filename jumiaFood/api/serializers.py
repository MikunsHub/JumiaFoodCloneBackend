from rest_framework import serializers
from .models import Vendor,Country,Business_Type,Menu,Order,OrderItems


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["country_name"]

class Business_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business_Type
        fields = ["type"]

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            "owner_name",
            "no_of_establishments",
            "country",
            "email",
            "business_type",
            "phone",
            "address"
        ]

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            "meal_name",
            "restaurant",
            "price"
        ]

class OrderItemsRetrieveSerializer(serializers.ModelSerializer):

    Price = serializers.SerializerMethodField('get_price')

    class Meta:
        model = OrderItems
        fields = ["menu","quantity","Price"]


    def get_price(self,obj):
        price = obj.menu.price
        quantity = obj.quantity
        return price * quantity


class OrderSerializer(serializers.ModelSerializer):
    
    item = OrderItemsRetrieveSerializer(
        many=True,
        source='orderitems_set',
        )

    class Meta:
        model = Order
        fields = (
            "id",
            "status",
            "item",
            "total_amount"
        )
        
    
    def create(self, validated_data):
        
        items_data = validated_data.pop('orderitems_set')
        order = Order.objects.create(**validated_data)
        
        for item in items_data:
            order.orderitems_set.create(**item)      

        return order

class OrderRetrieveSerializer(serializers.ModelSerializer):
    quantity = OrderItemsRetrieveSerializer(
        many=True,
        source='orderitems_set'
        )
    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "quantity",
            "total_amount",
        ]
        depth = 1

