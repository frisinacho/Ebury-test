from trades.models import Trades
from trades.serializers import TradeSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class TradeListAPI(ListCreateAPIView):
    queryset = Trades.objects.all()
    serializer_class = TradeSerializer


class TradeDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Trades.objects.all()
    serializer_class = TradeSerializer
