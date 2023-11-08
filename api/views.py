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
        if self.action in ['list']: return [permissions.AllowAny()]
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
        if self.action in ['list']: return [permissions.AllowAny()]
        elif self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticatedForCustomActions()]       
        return [permissions.IsAuthenticated()]             

    def list(self, request):
        queryset   = Player_Stats.objects.all()
        serializer = PlayerSerializer(queryset, many=True)        
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):        

        data = request.data   
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
    
        return Response(serializer.data, status=status.HTTP_201_CREATED, ) 