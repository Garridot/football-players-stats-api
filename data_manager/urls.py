from django.db import router
from django.urls import path, include, re_path
from . import views
from rest_framework.routers import DefaultRouter
from django.http import JsonResponse
from rest_framework.reverse import reverse


router = DefaultRouter()
router.register('players',views.PlayerView,basename='players') 
router.register('player_stats_general',views.GeneralStatsView,basename='player_stats') 
router.register('player_stats_position',views.StatsbyPositionView,basename='player_stats_by_position')


def api_root(request, format=None):
    return JsonResponse({
        "message": "Welcome to the Football Player Stats API.",
        "endpoints": {
            "players": reverse('players-list', request=request, format=format),
            "player_stats_general": reverse('player_stats-list', request=request, format=format),
            "player_stats_position": reverse('player_stats_by_position-list', request=request, format=format),
            "register": reverse('authentication:register', request=request, format=format),
            "token_obtain_pair": reverse('authentication:token_obtain_pair', request=request, format=format),
            "token_refresh": reverse('authentication:token_refresh', request=request, format=format),
        }
    })

api_root_pattern = [
    re_path(r'^$', api_root, name='api-root'),
]

urlpatterns = api_root_pattern + router.urls
