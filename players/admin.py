from django.contrib import admin

from .models import Player
from clubs.models import Club 
from games.models import Game
from trophies.models import Trophy
from individual_trophies.models import IndividualTrophy
from tables.models import Table
from coaches.models import Coach
from season_individual_player_stats.models import SeasonIndividualPlayerStats

admin.site.register(Player)
admin.site.register(Club)
admin.site.register(Game)
admin.site.register(Trophy)
admin.site.register(IndividualTrophy)
admin.site.register(Table)
admin.site.register(Coach)
admin.site.register(SeasonIndividualPlayerStats)