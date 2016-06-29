from trades.models import Trades
from trades.serializers import TradeSerializer, TradeListSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class TradeListAPI(ListCreateAPIView):
    queryset = Trades.objects.all()

    def get_serializer_class(self):
        return TradeSerializer if self.request.method == 'POST' else TradeListSerializer


class TradeDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Trades.objects.all()
    serializer_class = TradeSerializer
