from django.test import TestCase
from django_api.api.models.Room import Room


class ModelTestCase(TestCase):
    """This class defines the test suite for the room model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.name = "Buch B201"
        self.room = Room(name=self.name)

    def test_model_can_create_a_room(self):
        """Test the room model can create a room."""
        old_count = Room.objects.count()
        self.room.save()
        new_count = Room.objects.count()
        self.assertNotEqual(old_count, new_count)
