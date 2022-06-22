from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Club
from .serializers import ClubSerializer

class ClubViewSet(viewsets.ModelViewSet):
    '''
    '''

    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = [ 'name', 'country', 'state' ]