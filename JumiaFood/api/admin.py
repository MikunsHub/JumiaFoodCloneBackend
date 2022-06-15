from django.contrib import admin
from .models import *

admin.site.register([Country,Business_Type,Order,Menu,Driver,Delivery,Vendor])
