# -*- coding: utf-8 -*-
from django import forms
from django.utils.crypto import random
from trades.models import Trades


class TradesForm(forms.ModelForm):

    class Meta:
        model = Trades
        exclude = []


class CreateForm(forms.ModelForm):

    class Meta:
        model = Trades
        exclude = ['ID']
