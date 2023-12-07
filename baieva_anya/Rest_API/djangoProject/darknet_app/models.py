from django.db import models
class Products(models.Model):
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}||{self.price}$"

