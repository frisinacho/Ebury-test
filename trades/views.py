# -*- coding: utf-8 -*-
from django.http import HttpResponseNotFound
from django.shortcuts import render
from trades.models import Trades


def home(request):
    trades = Trades.objects.all().order_by('-date_booked')
    context = {
        'trades_list': trades
    }
    return render(request, 'trades/home.html', context)

def detail(request, pk):
    """
    :param request: HttpRequest
    :param pk: trade ID
    :return: HttpResponse
    """
    """
    # This is a try-except code that I don't like
    try:
        trade = Trades.objects.get(pk=pk)
    except Trades.DoesNotExist:
        trade = None
    except Trades.MultipleObjects:
        trade = None
    """

    possible_trades = Trades.objects.filter(pk=pk)
    trade = possible_trades[0] if len(possible_trades) == 1 else None
    if trade is not None:
        context = {
            'trade': trade
        }
        return render(request, 'trades/detail.html', context)
    else:
        return HttpResponseNotFound("404 Trade not found")
