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

router = routers.DefaultRouter()

router.register(r'players', PlayerViewSet)
router.register(r'clubs', ClubViewSet)
router.register(r'games', GameViewSet)
router.register(r'coaches', CoachViewSet)
router.register(r'trophies', TrophyViewSet)
router.register(r'individual_trophies', IndividualTrophyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
