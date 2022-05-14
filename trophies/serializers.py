from rest_framework import serializers

from .models import Trophy

class TrophySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trophy
        fields = ['id', 'season', 'competition', 'club_owner', 'created_at', 'updated_at']