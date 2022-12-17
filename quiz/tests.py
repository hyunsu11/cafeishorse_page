from django import views
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .views import helloAPI

class hello(APITestCase):
    
    def test_hello(self):
        response = self.client.get(reverse('hello'))
        print(response)
        print(response.data)
            
        #self.assertEqual(response.status_code,status.HTTP_200_OK)