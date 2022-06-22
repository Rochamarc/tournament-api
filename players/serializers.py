from rest_framework import serializers

from clubs.models import Club

from .models import Player

class ClubListing(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name']

class PlayerSerializer(serializers.HyperlinkedModelSerializer):

    current_club = ClubListing(many=False, read_only=True)

    class Meta:
        model = Player 
        fields = ['id', 'name', 'nationality', 'age', 'overall', 'current_club', 'position', 'matches', 'goals','assists', 
        'market_value', 'salary', 'height', 'weight', 'foot','average','created_at', 'updated_at' ]