# -*- coding: utf-8 -*-
from django import forms
from trades.models import Trades


class TradesForm(forms.ModelForm):

    class Meta:
        model = Trades
        exclude = []
