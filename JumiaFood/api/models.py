from django.db import models

from django.db import models
from user.models import  User

status_choices = (
    ("ordered", "ordered"),
    ("pending", "pending"),
    ("delivered", "delivered")
)


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

class Order(models.Model):
    status = models.CharField(max_length=30,choices=status_choices,default=status_choices[0][1])
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    items = models.ManyToManyField(Menu,through='OrderItems')
    total_amount = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)
 

class OrderItems(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu,on_delete=models.CASCADE)
    quantity =models.IntegerField(default=1)

    
# class Payment(models.Model):
#     pass



class Driver(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    address = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=20)
    driver_license = models.CharField(max_length=20) #make file field later

    def __str__(self):
        return f"{self.user.email}"

# class Delivery(models.Model):
#     driver = models.ForeignKey(Driver,on_delete=models.CASCADE)
#     order = models.ForeignKey(Order,on_delete=models.CASCADE)
#     delivery_time = models.DateTimeField()
    # status