# from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# class User(AbstractUser):
#     money = models.DecimalField(
#         max_digits=8, # max_digits=None,
#         decimal_places=2,
#         default=0.00
#     )

class User(models.Model):
    username = models.CharField(
        unique=True,
        max_length=30,
    )
    password = models.CharField(
        max_length=20,
    )
    email = models.EmailField(
        unique=True,
        blank=True,
        null=True
    )
    money = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.00
    )

    def __str__(self):
        return f"{self.username}"

class Card(models.Model):
    card_number = models.PositiveIntegerField(
        unique=True,
    )
    expiration_date = models.DateField() #TODO: models.CharField ???
    type = models.BooleanField()  #TODO: models.CharField ??? PositiveSmallIntegerField??? FK for table with card types ???
    money = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.00
    )
    currency = models.CharField(  #TODO: models.PositiveSmallIntegerField ??? FK for table with currencies ???
        max_length=3,
    )
    userID = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"XXXX XXXX XXXX {str(self.card_number)[-4:]}"

class Transaction(models.Model):
    amount = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    date_time = models.DateTimeField()
    type = models.PositiveSmallIntegerField()
    trader = models.CharField(max_length=100)
    cardID = models.ForeignKey(
        Card,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.date_time}"

class Limit(models.Model):
    amount = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    type = models.PositiveSmallIntegerField()
    period_start = models.DateField()
    period_end = models.DateField()
    target_date = models.DateField()
    currency = models.CharField(  #TODO: models.PositiveSmallIntegerField ??? FK for table with currencies ???
        max_length=3,
    )
    userID = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self}"
