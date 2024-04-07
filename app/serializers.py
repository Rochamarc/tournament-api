from rest_framework import serializers

from .models import Club, Player, Coach, SeasonIndividualPlayerStats, Competitions, Trophy

class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player 
        fields = "__all__"

class CoachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coach
        fields = "__all__"

class SeasonIndividualPlayerStatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SeasonIndividualPlayerStats
        fields = "__all__"

class CompetitionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competitions
        fields = "__all__"

class TrophySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trophy
        fields = "__all__"