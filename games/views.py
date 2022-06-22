from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Game 
from .serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = [ 'season', 'competition' ]