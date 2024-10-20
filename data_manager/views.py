from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

from .serializers import *
from .models import *

# Custom permission class to ensure only authenticated users can perform certain actions
class IsAuthenticatedForCustomActions(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow access only if the user is authenticated
        return request.user.is_authenticated

# ViewSet to handle CRUD operations for Player model
class PlayerView(ModelViewSet):        
    serializer_class   = PlayerSerializer
    queryset           = Players.objects.all()

    # Override to provide custom permissions for different actions
    def get_permissions(self):
        # Allow unauthenticated users to list and retrieve players
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        # Require authentication for create, update, and delete actions
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticatedForCustomActions()]       
        # Default permission: authenticated users only
        return [permissions.IsAuthenticated()]

    # List all players
    def list(self, request):
        queryset = Players.objects.all()
        serializer = PlayerSerializer(queryset, many=True)        
        return Response(serializer.data)

    # Create a new player
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# ViewSet to handle CRUD operations for Player_Stats model
class GeneralStatsView(ModelViewSet):        
    serializer_class   = PlayerStatsSerializer
    queryset           = Player_Stats.objects.all()

    # Override to provide custom permissions for different actions
    def get_permissions(self):
        # Allow unauthenticated users to list and retrieve stats
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        # Require authentication for create, update, and delete actions
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticatedForCustomActions()]       
        return [permissions.IsAuthenticated()]

    # List player stats based on optional filtering parameters
    def list(self, request):
        player_id = request.data.get('player')
        team = request.data.get('team')
        competition = request.data.get('competition')
        season = request.data.get('season')

        # Filter stats based on player, team, competition, and season if provided
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
        
    # Create or update player stats record
    def create(self, request, *args, **kwargs):
        player_id = request.data.get('player')
        team = request.data.get('team')
        competition = request.data.get('competition')
        season = request.data.get('season')

        # Check if the record exists for the given player, team, competition, and season
        existing_record = Player_Stats.objects.filter(
            player=player_id, team=team, competition=competition, season=season).first()

        if existing_record:
            # Update existing record if found
            serializer = self.get_serializer(existing_record, data=request.data, partial=True)
        else:
            # Create new record if none exists
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# ViewSet to handle CRUD operations for Stats_by_Position model
class StatsbyPositionView(ModelViewSet):   
    serializer_class   = StatsbyPositionSerializer
    queryset           = Stats_by_Position.objects.all()

    # Override to provide custom permissions for different actions
    def get_permissions(self):
        # Allow unauthenticated users to list and retrieve stats
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        # Require authentication for create, update, and delete actions
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticatedForCustomActions()]       
        return [permissions.IsAuthenticated()]

    # List stats by player and season, with optional filters
    def list(self, request):
        player_id = request.data.get('player')
        season = request.data.get('season')

        # Filter stats by player and season if provided
        queryset = Stats_by_Position.objects.all()
        if player_id is not None:
            queryset = queryset.filter(player=player_id)
        if season is not None:
            queryset = queryset.filter(season=season)
  
        serializer = StatsbyPositionSerializer(queryset, many=True)
        return Response(serializer.data)
        
    # Create or update stats by position record
    def create(self, request, *args, **kwargs):
        player_id = request.data.get('player')
        position = request.data.get('position')
        season = request.data.get('season')

        # Check if the record exists for the given player, position, and season
        existing_record = Stats_by_Position.objects.filter(
            player=player_id, position=position, season=season).first()

        if existing_record:
            # Update existing record if found
            serializer = self.get_serializer(existing_record, data=request.data, partial=True)
        else:
            # Create new record if none exists
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)    