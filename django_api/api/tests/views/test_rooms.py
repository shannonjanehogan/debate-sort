from django.test import TestCase
from django_api.api.models.Room import Room
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")

        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        # Since user model instance is not serializable, use its Id/PK
        self.room_data = {'name': 'Buch B201'}
        self.response = self.client.post(
            reverse('create'),
            self.room_data,
            format="json")

    def test_api_can_create_a_room(self):
        """Test the api has room creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get('/rooms/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_a_room(self):
        """Test the api can get a given room."""
        room = Room.objects.get(id=1)
        response = self.client.get(
            '/rooms/',
            kwargs={'pk': room.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, room)

    def test_api_can_update_room(self):
        """Test the api can update a given room."""
        room = Room.objects.get()
        change_room = {'name': 'Buch B201'}
        res = self.client.put(
            reverse('details', kwargs={'pk': room.id}),
            change_room, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_room(self):
        """Test the api can delete a room."""
        room = Room.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': room.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
