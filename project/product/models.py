from django.db import models
from django.contrib.auth.models import User
class brandModel(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) :
        return f"{self.name}"

class productModel(models.Model):
    image = models.ImageField(upload_to='media/uploads/')
    name = models.CharField(max_length=100)
    descrption = models.TextField()
    price = models.CharField(max_length=100)
    brand = models.ForeignKey(brandModel, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
    def __str__(self) :
        return f"{self.name}"
    
class UserCar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(productModel, on_delete=models.CASCADE)

class comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(productModel, on_delete=models.CASCADE)
    comment = models.TextField()
