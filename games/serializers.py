from logging.config import valid_ident
from rest_framework import serializers

from clubs.models import Club

from .models import Game


class ClubListing(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name']

class GameSerializer(serializers.HyperlinkedModelSerializer):
    
    home_team = ClubListing(many=False, read_only=False)
    away_team = ClubListing(many=False, read_only=False)

    class Meta:
        model = Game 
        fields = '__all__'

    def create(self, validated_data):
        home_data, away_data = validated_data.pop('home_team'), validated_data.pop('away_team')
        home_team, away_team = Club.objects.filter(name=home_data['name'])[0], Club.objects.filter(name=away_data['name'])[0]
        
        validated_data['home_team'] = home_team
        validated_data['away_team'] = away_team

        return Game.objects.create(**validated_data)
