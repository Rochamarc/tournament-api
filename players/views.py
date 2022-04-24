from rest_framework import viewsets
from rest_framework import permissions


from .models import Club, Player
from .serializers import PlayerSerializer, ClubSerializer

class ClubViewSet(viewsets.ModelViewSet):
    '''
    '''

    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    '''
    '''

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    