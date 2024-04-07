from rest_framework import viewsets

from .models import Club, Player, Coach, SeasonIndividualPlayerStats, Competitions
from .serializers import ClubSerializer, PlayerSerializer, CoachSerializer, CompetitionsSerializer 
from .serializers import SeasonIndividualPlayerStatsSerializer

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class CoachViewSet(viewsets.ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

class SeasonIndividualPlayerStatsViewSet(viewsets.ModelViewSet):
    queryset = SeasonIndividualPlayerStats.objects.all()
    serializer_class = SeasonIndividualPlayerStatsSerializer

class CompetitionsViewSet(viewsets.ModelViewSet):
    queryset = Competitions.objects.all()
    serializer_class = CompetitionsSerializer