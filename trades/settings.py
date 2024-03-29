# -*- coding: utf-8 -*-
from django.conf import settings

# Just G3 currencies for now
EURO = 'EUR'
POUND = 'GBP'
DOLLAR = 'USD'

DEFAULT_CURRENCIES = (
    (EURO, 'EUR'),
    (POUND, 'GBP'),
    (DOLLAR, 'USD'),
)

# More currencies could be added in the main settings.py
CURRENCIES = getattr(settings, 'CURRENCIES', DEFAULT_CURRENCIES)

# EMAIL Address
EMAIL_ADDRESS = getattr(settings, 'EMAIL_ADDRESS', 'test@ebury.com')
EMAIL_AVAILABLE = getattr(settings, 'EMAIL_AVAILABLE', True)
