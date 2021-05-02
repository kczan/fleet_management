from django.db import models

from cars import enums


class AbstractVehicle(models.Model):
    pass


class Car(AbstractVehicle):
    brand = models.CharField(verbose_name="Car brand", max_length=30, blank=False)
    model = models.CharField(verbose_name="Car model", max_length=30, blank=False)
    registration_number = models.CharField(
        verbose_name="Registration number", max_length=8, blank=False, unique=True
    )
    max_passenger_capacity = models.IntegerField(
        verbose_name="Maximum passenger capacity",
        choices=enums.MaxPassengerCapacityChoices.choices,
        default=enums.MaxPassengerCapacityChoices.ONE,
    )
    production_year = models.IntegerField(
        verbose_name="Year of production", blank=False
    )
    car_class = models.CharField(
        verbose_name="Car class",
        choices=enums.CarClassChoices.choices,
        default=enums.CarClassChoices.ECONOMY,
        max_length=20,
    )
    low_emission = models.BooleanField(
        verbose_name="Low emission engine (EV or Hybrid)", default=False
    )

    def __str__(self):
        return f"{self.brand} {self.model} {self.production_year}"
