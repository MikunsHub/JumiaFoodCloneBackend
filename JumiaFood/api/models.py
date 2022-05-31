from django.db import models

# Create your models here.

class Order(models.Model):
    payment_type = models.CharField(max_length=80)
    timestamp = models.DateTimeField()


class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()