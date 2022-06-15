from django.db import models

from django.db import models
from user.models import  User

#country and business_type can be simple choices
class Country(models.Model):
    country_name = models.CharField(max_length=80)

    def __str__(self):
        return f"<Country: {self.country_name}"

class Business_Type(models.Model):
    type = models.CharField(max_length=25)

    def __str__(self):
        return f"<Business_Type: {self.type}"

class Vendor(models.Model):
    owner_name = models.CharField(max_length=100)
    no_of_establishments = models.IntegerField()
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    email = models.EmailField()
    business_type = models.ForeignKey(Business_Type,on_delete=models.CASCADE)
    # name_of_store = 
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    # tin_doc = models.FileField()
    # incorporation_cert_doc = models.FileField()
    # owner_id = models.FileField()

    def __str__(self):
        return f"{self.owner_name}"

class Menu(models.Model):
    meal_name = models.CharField(max_length=100)
    restaurant = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return f"{self.meal_name}"

status_choices = (
    ("ordered", "ordered"),
    ("pending", "pending"),
    ("delivered", "delivered")
)

class Order(models.Model):
    status = models.CharField(max_length=30,choices=status_choices,default=status_choices[0][1])
    timestamp = models.DateTimeField(auto_now_add=True) #not sure
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    items = models.ManyToManyField(Menu, related_name="order_items")
    

    

# class OrderItems(models.Model):
#     order = models.ManyToManyField(Order, related_name="order_items")
#     quantity = models.IntegerField()
#     items = models.ForeignKey(Menu,on_delete=models.CASCADE)


# class Payment(models.Model):
#     pass

class Driver(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    dob = models.DateTimeField()
    vehicle_type = models.CharField(max_length=20)
    driver_license = models.FileField()

class Delivery(models.Model):
    driver = models.ForeignKey(Driver,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    delivery_time = models.DateTimeField()