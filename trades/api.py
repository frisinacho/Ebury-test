from trades.models import Trades
from trades.serializers import TradeSerializer
from rest_framework.generics import ListCreateAPIView


class TradeListAPI(ListCreateAPIView):

    queryset = Trades.objects.all()
    serializer_class = TradeSerializer

