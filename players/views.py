from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets


from .models import Player
from .serializers import PlayerSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    '''
    '''

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [ 'name', 'current_club', 'nationality', 'position' ]