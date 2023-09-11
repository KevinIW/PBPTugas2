from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255,default="")
    amount = models.IntegerField(default=0)
    description = models.TextField(default = "")