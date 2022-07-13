from rest_framework import permissions

class CustomerViewOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_customer == True:
            return True
   
class DriverViewOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_driver == True:
            return True
            