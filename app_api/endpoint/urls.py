from django.urls import path
from . import views

urlpatterns = [
    path("restaurants/", views.get_restaurants, name="get_restaurants"),
    path("couriers/", views.get_couriers, name="get_couriers"),
    path("products/", views.get_products, name="get_products"),
    path("orders/", views.get_orders, name="get_orders"),
]
