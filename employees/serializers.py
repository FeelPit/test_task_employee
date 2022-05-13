from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from .models import Employee
from cities_light.models import City, Country

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'phone', 'city', 'country')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'display_name', 'country')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')