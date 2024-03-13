from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Customers
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# all of our Products
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(null=True, blank=True, default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=30, default='', blank=True,null=True)
    description2 = models.TextField(max_length=10000, default='', blank=True,null=True)
    image = models.ImageField(upload_to='uploads/product/')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6, null=True, blank=True)

    def __str__(self):
        return self.name
class Books(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=30, default='', blank=True, null=True)
    description2 = models.TextField(max_length=10000, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/', null=True)
    file = models.FileField(null=True, blank=True, upload_to='Files')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product)

