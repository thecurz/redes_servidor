from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    rating = models.FloatField()
    cuisine_type = models.CharField(max_length=50)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return self.name


class Courier(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_time = models.DateTimeField(auto_now_add=True)
    delivery_address = models.CharField(max_length=200)
    status = models.CharField(max_length=50, default="pending")


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return self.name


class Receipt(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    pago = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
