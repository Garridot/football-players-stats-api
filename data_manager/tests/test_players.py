from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient
from authentication.models import User
from rest_framework import status
from django.test import TestCase
from data_manager.models import Players
            
class PlayerViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail', password='testpassword')
        self.refresh_token = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh_token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def create_player(self, data):
        return self.client.post('/players/', data, format='json')

    def test_list_players(self):
        response = self.client.get('/players/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def player_created(self):
        return Players.objects.create(
            name='Player One',
            age=20,
            date_of_birth='2023-11-02',
            nationality='Country One',
            position='Position Player',
            current_club='Club One'
        )    

    def create_test_player(self):
        return {
            "name": "Player One",
            "age": -19,
            "date_of_birth": '2023-11-02',
            "nationality": 'Country One',
            "position": 'Position Player',
            "current_club": "Club One"
        } 

    def test_create_empty_player(self):
        data = self.create_test_player()
        data["name"] = ""            
        response = self.create_player(data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Players.objects.count(), 0)

    def test_age_invalid(self):        
        data = self.create_test_player()
        data["age"] = -19 
        response = self.create_player(data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Players.objects.count(), 0)

    def test_date_invalid(self):
        # test to ensure that the 'date of birth' field is entered in the format 'YYYY-MM-DD'
        data = self.create_test_player()
        data["date_of_birth"] = '2023-June-Sunday'        
        response = self.create_player(data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Players.objects.count(), 0)

    def test_update_player(self):
        player = self.player_created()
        data = self.create_test_player()
        data["name"] = 'Player Updated' 
        data["age"]  = 19
        data["nationality"]  = 'España'
       
        response = self.client.put(f'/players/{player.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        player.refresh_from_db()
        self.assertEqual(player.name, "Player Updated")
        self.assertEqual(player.age, 19)
        self.assertEqual(player.nationality, "España")

    def test_delete_player(self):
        player = self.player_created()
        response = self.client.delete(f'/players/{player.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Players.DoesNotExist):
            player.refresh_from_db()
            