from rest_framework import generics, permissions
from .serializers import RoomSerializer, TeamSerializer, JudgeSerializer, SortedRoomSerializer, VPIPreferenceSerializer, SignUpPreferenceSerializer, MemberSerializer
from api.models.Room import Room
from api.models.Team import Team
from api.models.Judge import Judge
from api.models.SortedRoom import SortedRoom
from api.models.VPIPreference import VPIPreference
from api.models.SignUpPreference import SignUpPreference
from api.models.Member import Member
from .permissions import IsOwner

class RoomCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new room."""
        serializer.save()

class RoomDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class TeamCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new room."""
        serializer.save()

class TeamDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class JudgeCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Judge.objects.all()
    serializer_class = JudgeSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new room."""
        serializer.save()

class JudgeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Judge.objects.all()
    serializer_class = JudgeSerializer

class SortedRoomCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = SortedRoom.objects.all()
    serializer_class = SortedRoomSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new room."""
        serializer.save()

class SortedRoomDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = SortedRoom.objects.all()
    serializer_class = SortedRoomSerializer

class VPIPreferenceCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = VPIPreference.objects.all()
    serializer_class = VPIPreferenceSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new room."""
        serializer.save()

class VPIPreferenceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = VPIPreference.objects.all()
    serializer_class = VPIPreferenceSerializer

class SignUpPreferenceCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = SignUpPreference.objects.all()
    serializer_class = SignUpPreferenceSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new room."""
        serializer.save()

class SignUpPreferenceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = SignUpPreference.objects.all()
    serializer_class = SignUpPreferenceSerializer

class MemberCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new room."""
        serializer.save()

class MemberDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
