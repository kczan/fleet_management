from django.urls import path

from api import views


car_list = views.CarAPIViewset.as_view({"get": "list"})
car_detail = views.CarAPIViewset.as_view({"get": "retrieve_by_query_params_id"})
car_create = views.CarAPIViewset.as_view({"post": "create"})
car_update = views.CarAPIViewset.as_view({"post": "update"})
car_delete = views.CarAPIViewset.as_view({"delete": "destroy"})

urlpatterns = [
    path("car:list", car_list),
    path("car:retrieve", car_detail),
    path("car:create", car_create),
    path("car:update/<int:id>", car_update),
    path("car:delete/<int:id>", car_delete),
]
