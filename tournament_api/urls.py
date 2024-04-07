"""tournament_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from games.views import GameViewSet
from players.views import PlayerViewSet
from clubs.views import ClubViewSet
from coaches.views import CoachViewSet
from trophies.views import TrophyViewSet
from individual_trophies.views import IndividualTrophyViewSet
from season_individual_player_stats.views import SeasonIndividualPlayerStatsViewSet
from tables.views import TableViewSet

# Changing versioning
from app.views import ClubViewSet as ClubViewSetV2
from app.views import PlayerViewSet as PlayerViewSetV2
from app.views import CoachViewSet as CoachViewSetV2

router = routers.DefaultRouter()


router.register(r'v1/players', PlayerViewSet)
router.register(r'v1/clubs', ClubViewSet)
router.register(r'v1/games', GameViewSet)
router.register(r'v1/coaches', CoachViewSet)
router.register(r'v1/trophies', TrophyViewSet)
router.register(r'v1/individual_trophies', IndividualTrophyViewSet)
router.register(r'v1/season_individual_player_stats', SeasonIndividualPlayerStatsViewSet)
router.register(r'v1/tables', TableViewSet)

router.register(r'v2/clubs', ClubViewSetV2)
router.register(r'v2/players', PlayerViewSetV2)
router.register(r'v2/coaches', CoachViewSetV2)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
