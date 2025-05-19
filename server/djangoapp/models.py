from django.db import models

# CarMake model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Car Make: {self.name}"

# CarModel model
class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=10, choices=CAR_TYPES, default=SEDAN)
    year = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.car_make.name}) - {self.car_type} - {self.year.year}"
