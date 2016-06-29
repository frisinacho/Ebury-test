from rest_framework.views import APIView
from rest_framework.response import Response
from trades.models import Trades
from trades.serializers import TradeSerializer


class TradeListAPI(APIView):

    def get(self, request):
        trades = Trades.objects.all()
        serializer = TradeSerializer(trades, many=True)
        return Response(serializer.data)
