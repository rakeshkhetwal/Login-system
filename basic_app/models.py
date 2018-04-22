from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserAmount(models.Model):



    amounts = models.DecimalField(default=4000, max_digits=6, decimal_places=2)




