from django.urls import path,include
from .views import (
    CountryCreateListApiView,
    Business_TypeCreateListApiView,
    VendorCreateListApiView,
    MenuCreateListApiView,
    OrderCreateListApiView,
    OrderUpdateApiView,
    OrderRetrieveApiView,
    OrderDeleteApiView
)

urlpatterns = [
    path('countries/',CountryCreateListApiView.as_view()),
    path('business_type/',Business_TypeCreateListApiView.as_view()),
    path('vendor/',VendorCreateListApiView.as_view()),
    path('menu/',MenuCreateListApiView.as_view()),
    path('order/',OrderCreateListApiView.as_view()),
    path('<int:pk>/order/',OrderUpdateApiView.as_view()),
    path('order/<int:pk>/',OrderRetrieveApiView.as_view()),
    path('order/<int:pk>/delete/',OrderDeleteApiView.as_view()),
]