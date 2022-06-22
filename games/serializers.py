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
        fields = [
            'id',
            'home_team',
            'away_team',
            'competition',
            'season',
            'hour',
            'score',
            'stadium',
            'home_shots',
            'home_shots_on_target',
            'home_fouls',
            'home_tackles',
            'home_saves',
            'home_ball_possession',
            'home_offsides',
            'home_freekicks',
            'away_shots',
            'away_shots_on_target',
            'away_fouls',
            'away_tackles',
            'away_saves',
            'away_ball_possession',
            'away_offsides',
            'away_freekicks',
            'created_at',
            'updated_at'
        ]