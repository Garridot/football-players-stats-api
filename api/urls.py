from django.db import router
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('players',views.PlayerView,basename='players') 
router.register('player_stats',views.PlayerStatsView,basename='player_stats') 

urlpatterns = [ 
    path('api/',include(router.urls)),    
]    