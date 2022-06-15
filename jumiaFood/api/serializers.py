from rest_framework import serializers
from .models import Vendor,Country,Business_Type,Menu,Order


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

class OrderSerializer(serializers.ModelSerializer):
    # total_amt = serializers.SerializerMethodField(method_name='get_total_amt')
    class Meta:
        model = Order
        fields = [
            "status",
            "items",
            # "total_amt"
        ]
        depth = 1

    # def get_total_amt(self,instance):
    #     request = self.context.get('request')
    #     model.items

