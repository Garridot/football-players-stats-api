from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient
from authentication.models import User
from rest_framework import status
from django.test import TestCase
from api.models import Players

            
class PlayerViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email='testuser@gmail', password='testpassword')
        self.refresh_token = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh_token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def create_player(self, data):
        return self.client.post('/api/players/', data, format='json')

    def test_list_players(self):
        response = self.client.get('/api/players/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_empty_player(self):
        data = {
            "name": "",
            "age": 19,
            "date_of_birth": '2023-11-02',
            "nationality": 'España',
            "position": 'Position Player',
            "current_club": "Club One"
        }
        response = self.create_player(data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Players.objects.count(), 0)

    def test_age_invalid(self):
        data = {
            "name": "Player One",
            "age": -19,
            "date_of_birth": '2023-11-02',
            "nationality": 'España',
            "position": 'Position Player',
            "current_club": "Club One"
        }
        response = self.create_player(data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Players.objects.count(), 0)

    def test_date_invalid(self):
        data = {
            "name": "Player One",
            "age": 19,
            "date_of_birth": '2023-June-Sunday',
            "nationality": 'España',
            "position": 'Position Player',
            "current_club": "Club One"
        }
        response = self.create_player(data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Players.objects.count(), 0)

    def test_update_player(self):
        player = Players.objects.create(
            name='Player One',
            age=20,
            date_of_birth='2023-11-02',
            nationality='Country One',
            position='Position Player',
            current_club='Club One'
        )
        data = {
            "name": "Player Updated",
            "age": 19,
            "date_of_birth": '2023-11-02',
            "nationality": 'España',
            "position": 'Position Player',
            "current_club": "Club One"
        }
        response = self.client.put(f'/api/players/{player.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        player.refresh_from_db()
        self.assertEqual(player.name, "Player Updated")
        self.assertEqual(player.age, 19)
        self.assertEqual(player.nationality, "España")

    def test_delete_player(self):
        player = Players.objects.create(
            name='Player One',
            age=20,
            date_of_birth='2023-11-02',
            nationality='Country One',
            position='Position Player',
            current_club='Club One'
        )
        response = self.client.delete(f'/api/players/{player.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Players.DoesNotExist):
            player.refresh_from_db()
            