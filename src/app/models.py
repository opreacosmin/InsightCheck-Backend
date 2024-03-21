from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    userID = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    money = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.00
    )

    def __str__(self):
        return f"PROFILE: {self.userID}"

class Card(models.Model):
    card_number = models.PositiveBigIntegerField(
        unique=True,
    )
    expiration_date = models.DateField()
    type = models.BooleanField() #0-credit, 1-debit
    money = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.00
    )
    currency = models.CharField(
        max_length=3,
    )
    profileID = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"CARD: XXXX XXXX XXXX {str(self.card_number)[-4:]}"

class TransactionType(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return f"TRANSACTION TYPE: {self.description}"

class Transaction(models.Model):
    amount = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    date_time = models.DateTimeField()
    trader = models.CharField(max_length=100)
    cardID = models.ForeignKey(
        Card,
        on_delete=models.CASCADE
    )
    transactionTypeID = models.ForeignKey(
        TransactionType,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"TRANSACTION: {self.date_time} | {self.trader}"

class LimitType(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return f"LIMIT TYPE: {self.description}"

class Limit(models.Model):
    amount = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    recurring = models.BooleanField() #0-false, 1-true
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    period_start = models.DateField()
    period_end = models.DateField()
    currency = models.CharField(
        max_length=3,
    )
    profileID = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    LimitTypeID = models.ForeignKey(
        LimitType,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"LIMIT: {self.name} | {self.period_start} - {self.period_end} | {self.amount} {self.currency}"

class SavingsPlan(models.Model):
    name = models.CharField(max_length=50)
    target_amount = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    current_amount = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )
    profileID = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"SAVINGS PLAN: {self.name} | {self.target_amount} | {self.current_amount}"

