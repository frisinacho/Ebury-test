# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import Trades


class TradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trades
