from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse
from authentication.models import User


class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register') 
        self.login_url    = reverse('token_obtain_pair') 

    def test_user_registration(self):
        data = {            
            'email': 'testuser@example.com',
            'password': 'Testpassword500$'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_user_authentication(self):
        user = User.objects.create_user(email='testuser@example.com', password='Testpassword500$')
        data = {
            'email': 'testuser@example.com',
            'password': 'Testpassword500$'
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)  

    def test_invalid_len_password(self):  
        # The password must be at least 12 characters. 
        data = {            
            'email': 'testuser@example.com',
            'password': 'Testpasswor'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST) 

    def test_invalid_password_1(self):   
        # The password must include at least one uppercase letter, one lowercase letter, one number, and one special character.
        data = {            
            'email': 'testuser@example.com',
            'password': 'Testpassword500'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST) 

    def test_invalid_password_2(self): 
        # The password cannot be the same as the email.
        data = {            
            'email': 'testuser@example.com',
            'password': 'testuser@example.com'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)            
