from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from cities_light.models import City, Country

class Employee(models.Model):
    name = models.CharField(max_length=100, null=False)
    phone = PhoneNumberField(null=False, blank=False, unique=True) #We are using Phone Number model from library phonenumber_field
    city = models.ForeignKey(City, on_delete=models.CASCADE) #We are using foreign key from City of library cities_light
    country = models.ForeignKey(Country, on_delete=models.CASCADE) #We are using foreign key from Country of library cities_light

    def __str__(self):
        return self.name
