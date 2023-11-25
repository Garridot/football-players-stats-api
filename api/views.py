from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

from .serializers import *
from .models import *

# Create your views here.


class IsAuthenticatedForCustomActions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated: return True
        return False


class PlayerView(ModelViewSet):        
    serializer_class   = PlayerSerializer
    queryset           = Players.objects.all() 

    def get_permissions(self):
        if self.action in ['list','retrieve']: return [permissions.AllowAny()]
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticatedForCustomActions()]       
        return [permissions.IsAuthenticated()]  

    def list(self, request):
        queryset   = Players.objects.all()
        serializer = PlayerSerializer(queryset, many=True)        
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):        

        data = request.data   
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
    
        return Response(serializer.data, status=status.HTTP_201_CREATED, )   


class PlayerStatsView(ModelViewSet):        
    serializer_class   = PlayerStatsSerializer
    queryset           = Player_Stats.objects.all() 

    def get_permissions(self):
        if self.action in ['list','retrieve']: return [permissions.AllowAny()]
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticatedForCustomActions()]       
        return [permissions.IsAuthenticated()]             

    def list(self, request):

        player_id = request.data.get('player')
        team = request.data.get('team')
        competition = request.data.get('competition')
        season = request.data.get('season')

        # Check if a record already exists for the specified player, team, competition, and season
        queryset = Player_Stats.objects.all()
        if player_id is not None:
            queryset = queryset.filter(player=player_id)
        if team is not None:
            queryset = queryset.filter(team=team)
        if competition is not None:
            queryset = queryset.filter(competition=competition)
        if season is not None:
            queryset = queryset.filter(season=season)
  
        serializer = PlayerStatsSerializer(queryset, many=True)        
        return Response(serializer.data)
        
   
    def create(self, request, *args, **kwargs):
        # Extract relevant data from the request
        player_id = request.data.get('player')
        team = request.data.get('team')
        competition = request.data.get('competition')
        season = request.data.get('season')

        # Check if a record already exists for the specified player, team, competition, and season
        existing_record = Player_Stats.objects.filter(player=player_id, team=team, competition=competition, season=season).first()

        if existing_record:
            # If the record exists, update it
            serializer = self.get_serializer(existing_record, data=request.data, partial=True)
        else:
            # If the record doesn't exist, create a new one
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)    