from rest_framework import serializers

from .models import Player, Club

class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta  :
        model = Club
        fields = ['name', 'country', 'state', 'coeff', 'formation', 'created_at', 'updated_at']

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player 
        fields = ['name', 'nationality', 'age', 'overall', 'current_club', 'position', 'matches', 'goals','assists', 'created_at', 'updated_at' ]