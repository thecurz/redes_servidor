from django.urls import path
from . import views

urlpatterns = [
    path("restaurants/", views.get_restaurants, name="get_restaurants"),
    path("restaurants", views.create_restaurant, name="create_restaurant"),
    path("couriers/", views.get_couriers, name="get_couriers"),
    path("couriers", views.create_courier, name="create_courier"),
    path("products/", views.get_products, name="get_products"),
    path("products", views.create_product, name="create_product"),
    path(
        "products/<int:restaurant_id>/",
        views.get_products_by_restaurant,
        name="get_products_by_restaurant",
    ),
    path("create_receipt/", views.create_receipt, name="create-receipt"),
    path("orders/", views.get_orders, name="get_orders"),
    path("orders", views.create_order, name="create_order"),
]
