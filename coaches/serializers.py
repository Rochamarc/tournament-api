from rest_framework import serializers

from .models import Coach

class CoachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta  :
        model = Coach
        fields = ['id','name', 'nationality', 'age', 'formation', 'play_mode', 'current_club', 'created_at', 'updated_at']