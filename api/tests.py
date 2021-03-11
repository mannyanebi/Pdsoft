# from django.test import TestCase
import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from .models import ContactDetail
from .serializers import ContactDetailSerializer

# Create your tests here.
class ContactDetailTestCase(APITestCase):
    
    def test_contactdetail(self):
        data = {"fullname": "Tester 01", "email": "tester@pdsoft.app", 
        "message": "I am an automated test"}

        response = self.client.post("/contactus/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)