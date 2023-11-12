from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient
from authentication.models import User
from rest_framework import status
from django.test import TestCase
from api.models import *

class PlayerViewSetTestCase(TestCase):    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail', password='testpassword')
        self.refresh_token = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh_token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.player = self.create_player()

    def create_player(self):
        return Players.objects.create(
            name= 'Player One', 
            age= 20, 
            date_of_birth= '2023-11-02', 
            nationality= 'Country One', 
            position='Position Player', 
            current_club="Club One"
        )

    def create_stats(self, data):
        return self.client.post('/api/player_stats/', data, format='json') 

    def create_stats_data(self):
        return {
            "player": self.player.id,
            "team": "Team One", 
            "competition": 10,  
            "goals": 20,
            "assists": 30,
            "games": 40, 
            "wins": 50,    
            "draws": 60,
            "defeats": 70, 
            "team_goals": 80,
            "minutes_played": 2000,
            "season": "2001-2002",
        }

    def test_player_not_exists(self):
        data = self.create_stats_data()
        data["player"] = 2

        response = self.create_stats(data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Player_Stats.objects.count(), 0)    

    def test_number_invalid(self):
        data = self.create_stats_data()
        data["goals"] = "-50"
        response = self.create_stats(data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Player_Stats.objects.count(), 0)    

    def test_season_invalid(self):
        # test to ensure that the 'season' field is entered in the format 'YYYY-YYYY'
        data = self.create_stats_data()
        data["season"] = "01/02"
        response = self.create_stats(data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Player_Stats.objects.count(), 0)    
