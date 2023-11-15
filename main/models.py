from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,default="")
    amount = models.IntegerField(default=0)
    description = models.TextField(default = "")


