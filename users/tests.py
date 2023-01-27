from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.forms import UserRegistrationForm
from users.models import User


class sernameUserRegistrationViewTestCase(TestCase):

    def setUp(self) -> None:
        self.data = {
            'first_name': 'Valk', 'last_name': 'Kalin',
            'username': 'alesa', 'email': 'sdert@gmail.com',
            'password1': '12345678Qw', 'password2': '12345678Qw',
        }

        self.path = reverse('users:registration')

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Регістрація')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_post(self):
        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, self.data)

        # check creating of user
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        # for debug mode
        # a=1
