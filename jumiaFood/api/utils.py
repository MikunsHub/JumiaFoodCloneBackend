from django.db import models
from rest_framework.response import Response
from .models import Delivery,Order
from .serializers import DeliverySerializer


def create_delivery(order_id):
    order = Order.objects.get(id=order_id)
    delivery = Delivery.objects.create(order=order)
    print("working")
    return Response({"message":"successfully created a delivery instance"})

# {'id': 3, 'delivery': 2, 'driver': 16, 'driver_status': 'accepted'}
def update_order_status(delivery_id):
    delivery = Delivery.objects.get(id=delivery_id)

    order_id = delivery.order.id
    order_instance = Order.objects.get(id=order_id)
    order_instance.status = "in_transit"
    #raise exception for objects that have been updated once
    print(order_instance)
    order_instance.save()
    print("working")

def order_complete_status(delivery_id):
    delivery = Delivery.objects.get(id=delivery_id)

    order_id = delivery.order.id
    order_instance = Order.objects.get(id=order_id)
    order_instance.status = "delivered"
    print(order_instance)
    order_instance.save()
    print("order delivered")