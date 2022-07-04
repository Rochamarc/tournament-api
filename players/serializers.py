from wsgiref import validate
from rest_framework import serializers

from clubs.models import Club

from .models import Player

class ClubListing(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name']

class PlayerSerializer(serializers.HyperlinkedModelSerializer):

    current_club = ClubListing(many=False, read_only=False)

    def create(self, validate_data):
        club_data = validate_data.pop('current_club')
        club = Club.objects.filter(name=club_data['name'])[0]
        validate_data['current_club'] = club
        player = Player.objects.create(**validate_data)
        return player

    class Meta:
        model = Player 
        fields = ['id', 'name', 'nationality', 'age', 'overall', 'current_club', 'position', 'matches', 'goals','assists', 
        'market_value', 'salary', 'height', 'weight', 'foot','average','created_at', 'updated_at' ]

    