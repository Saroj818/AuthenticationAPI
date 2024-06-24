import base64
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import HTTP_HEADER_ENCODING, status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token


class Authcase(TestCase):
    def setUp(self):
        username = "test1"
        password = "test@1234"

        # Create database user. It needs to be created with django set_password function.
        User.objects.create_user(username=username, password=password)

        # Generate base64 credentials string
        credentials = f"{username}:{password}"
        self.base64_credentials = base64.b64encode(
            credentials.encode(HTTP_HEADER_ENCODING)
        ).decode(HTTP_HEADER_ENCODING)


    def test_basic_auth(self):
        """This test basic auth"""
        response = self.client.get(
            path="/api/basic/auth",
            HTTP_AUTHORIZATION=f"Basic {self.base64_credentials}",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK )
        self.assertEqual(response.data['Data'],'Validation succesfull for Basic Authentication')
       
    def test_auth_token(self):
        """This validates obtain auth token"""
        response = self.client.post(
            path="/api/token/auth",
            data = {"username":"test1", "password":"test@1234"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK )

    def test_jwt_token_generation_refresh(self):
        """This test the generation of JWT token."""
        response = self.client.post(
            path="/api/jwt/token/",
            data = {"username":"test1", "password":"test@1234"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK )
        refresh_token = response.data["refresh"]
        response = self.client.post(
            path="/api/jwt/refresh/",
            data = {"refresh":refresh_token}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK )
