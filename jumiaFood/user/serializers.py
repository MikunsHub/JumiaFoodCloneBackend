from rest_framework import serializers
from .models import User
from api.models import Driver

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["phone_number","username","email","password","is_driver","is_customer"]
        extra_kwargs = {
            'password': {'write_only':True}
        }

    def create(self,validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class DriverRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Driver
        fields = [
            'user',
            'address',
            'vehicle_type',
            'driver_license'
        ]

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of driver
        :return: returns a successfully created driver record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        driver, created = Driver.objects.update_or_create(user=user,
                            address=validated_data.pop('address'),
                            vehicle_type=validated_data.pop('vehicle_type'),
                            driver_license=validated_data.pop('driver_license')
                            )
        return driver
