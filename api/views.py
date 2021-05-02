import django_filters.rest_framework
import json

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from cars.models import Car
from cars.serializers import CarSerializer


class CarAPIViewset(ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = (
        "model",
        "brand",
        "production_year",
        "registration_number",
        "max_passenger_capacity",
        "id",
        "car_class",
        "low_emission",
    )
    lookup_field = "id"

    def retrieve_by_query_params_id(self, request, *args, **kwargs):
        if id := self.request.query_params.get("id", None):
            try:
                instance = Car.objects.get(id=id)
                serializer = self.get_serializer(instance)
                data = serializer.data
                return Response(data, status=status.HTTP_200_OK)
            except ObjectDoesNotExist:
                return Response(
                    {"detail": "Car with this id doesn't exist in our database."}
                )
        return Response(
            {
                "detail": "Please provide keyword id in query params to get specific entry."
            }
        )
