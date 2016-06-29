# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import Trades


class TradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trades


class TradeListSerializer(TradeSerializer):

    class Meta(TradeSerializer.Meta):
        fields = ('sell_currency', 'sell_amount', 'buy_currency', 'buy_amount', 'rate', 'date_booked')
