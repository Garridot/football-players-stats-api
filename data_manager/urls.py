from django.db import router
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('players',views.PlayerView,basename='players') 
router.register('player_stats_general',views.GeneralStatsView,basename='player_stats') 
router.register('player_stats_position',views.StatsbyPositionView,basename='player_stats_by_position') 

urlpatterns = [ 
    path('',include(router.urls)),    
]    