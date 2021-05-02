from django.db import models
from django.utils.translation import gettext_lazy as _


class MaxPassengerCapacityChoices(models.IntegerChoices):
    ONE = 1
    THREE = 3
    FOUR = 4
    SIX = 6
    EIGHT = 8


class CarClassChoices(models.TextChoices):
    FIRST = "FRST", _("First class")
    BUSINESS = "BSNS", _("Business class")
    ECONOMY = "ECON", _("Economy class")
