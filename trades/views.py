# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.utils.crypto import random
from trades.models import Trades
from trades.forms import TradesForm, CreateForm
from django.core.urlresolvers import reverse
from django.views.generic import View
from trades.settings import EMAIL_ADDRESS, EMAIL_AVAILABLE


class HomeView(View):
    def get(self, request):
        trades_list = Trades.objects.all().order_by('-date_booked')
        paginator = Paginator(trades_list, 5)   # Show 5 trades per page

        page = request.GET.get('page')
        try:
            trades = paginator.page(page)
        except PageNotAnInteger:
            # If not an integer, return first page
            trades = paginator.page(1)
        except EmptyPage:
            # If out of range, return last page
            trades = paginator.page(paginator.num_pages)

        return render(request, 'trades/home.html', {'trades_list': trades})


class DetailView(View):
    def get(self, request, pk):
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


class CreateView(View):
    def get(self, request):
        """
        :param request: HttpRequest
        :return: HttpResponse
        """
        form = CreateForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'trades/new_trade.html', context)

    def post(self, request):
        """
        :param request: HttpRequest
        :return: HttpResponse
        """
        success_message = ''
        request.POST = request.POST.copy()

        # Generate Auto-ID
        trade_id = 'TR'
        for i in range(7):
            trade_id += random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        while Trades.objects.filter(ID=[trade_id]).count():
            trade_id = 'TR'
            for i in range(7):
                trade_id += random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        request.POST['ID'] = trade_id
        form = TradesForm(request.POST)
        if form.is_valid():
            new_trade = form.save()  # Save and return the trade
            if EMAIL_AVAILABLE:
                send_mail(
                    'New trade',
                    'The trade ' + new_trade.pk +
                    ' has been created on ' + new_trade.date_booked +
                    ' with next values:\n' +
                    new_trade.sell_currency + ' ' + new_trade.sell_amount +
                    ' -> ' + new_trade.rate + ' -> ' +
                    new_trade.buy_currency + ' ' + new_trade.buy_amount,
                    'new_trade@ebury.com',
                    EMAIL_ADDRESS,
                    fail_silently=False,
                )
            form = TradesForm()
            success_message = 'Successfully saved! '
            success_message += '<a href="{0}">'.format(reverse('trade_detail', args=[new_trade.pk]))
            success_message += 'View trade'
            success_message += '</a>'
        context = {
            'form': form,
            'success_message': success_message
        }
        return render(request, 'trades/new_trade.html', context)


class DeleteView(View):
    def get(self, request, pk):
        """
        :param request: HttpRequest
        :param pk: trade ID
        :return: HttpResponse
        """

        possible_trades = Trades.objects.filter(pk=pk)
        trade = possible_trades[0] if len(possible_trades) == 1 else None
        if trade is not None:
            context = {
                'trade': trade
            }
            return render(request, 'trades/delete.html', context)
        else:
            return HttpResponseNotFound("404 Trade not found")

    def post(self, request, pk):
        possible_trades = Trades.objects.filter(pk=pk)
        trade = possible_trades[0] if len(possible_trades) == 1 else None
        trade.delete()
        return HttpResponseRedirect('/')
