from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant, Courier, Product, Order
from .serializers import (
    RestaurantSerializer,
    CourierSerializer,
    ProductSerializer,
    OrderSerializer,
)


@api_view(["GET"])
def get_restaurants(request):
    queryset = Restaurant.objects.all()
    serializer = RestaurantSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_couriers(request):
    queryset = Courier.objects.all()
    serializer = CourierSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_products(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_orders(request):
    queryset = Order.objects.all()
    serializer = OrderSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
