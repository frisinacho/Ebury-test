from __future__ import unicode_literals

from django.db import models

# Just G3 currencies for now
EURO = 'EUR'
POUND = 'GBP'
DOLLAR = 'USD'

CURRENCIES = (
    (EURO, 'EUR'),
    (POUND, 'GBP'),
    (DOLLAR, 'USD'),
)


class Trades(models.Model):

    ID = models.CharField(max_length=9, primary_key=True)
    sell_currency = models.CharField(max_length=3, choices=CURRENCIES)
    sell_amount = models.DecimalField(max_digits=9, decimal_places=2)
    buy_currency = models.CharField(max_length=3, choices=CURRENCIES)
    buy_amount = models.DecimalField(max_digits=9, decimal_places=2)
    rate = models.FloatField(default="")
    date_booked = models.DateTimeField(auto_now_add=True)   # Automatic generation when created
