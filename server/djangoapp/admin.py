from django.contrib import admin
from .models import CarMake, CarModel

# Register the models
admin.site.register(CarMake)
admin.site.register(CarModel)
