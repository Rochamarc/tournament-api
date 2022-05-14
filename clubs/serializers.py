from rest_framework import serializers

from .models import Club

from trophies.models import Trophy
from players.models import Player 
from coaches.models import Coach 

class TrophiesListing(serializers.ModelSerializer):
    class Meta:
        model = Trophy 
        fields = [ 'id', 'competition', 'season' ]

class PlayersListing(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = [ 'id', 'name', 'position', 'age', 'nationality', 'overall' ]

class CoachesListing(serializers.ModelSerializer):
    class Meta:
        model = Coach 
        fields = [ 'id', 'name', 'nationality', 'age', 'formation', 'play_mode' ]


class ClubSerializer(serializers.HyperlinkedModelSerializer):

    trophies = TrophiesListing(many=True, read_only=True)    
    players = PlayersListing(many=True, read_only=True) 
    coach = CoachesListing(many=True, read_only=True)

    class Meta  :
        model = Club
        fields = ['id','name', 'country', 'state', 'coeff', 'formation', 'players', 'coach', 'trophies', 'created_at', 'updated_at']
