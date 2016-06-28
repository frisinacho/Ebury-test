# -*- coding: utf-8 -*-
from django.shortcuts import render
from trades.models import Trades


def home(request):
    trades = Trades.objects.all()
    context = {
        'trades_list': trades
    }
    return render(request, 'trades/home.html', context)
