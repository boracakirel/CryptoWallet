from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    price = models.DecimalField(decimal_places=10, max_digits=100)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(decimal_places=10, max_digits=100)
    user = models.ManyToManyField(User, blank=True, related_name='transactions')
    coin_id = models.CharField(max_length=100)

