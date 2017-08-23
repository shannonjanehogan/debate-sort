from rest_framework import generics
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
# from .csrf_exempt import CsrfExemptSessionAuthentication
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .models.DebaterPreference import DebaterPreference
from .models.Judge import Judge
from .models.Member import Member
from .models.Room import Room
from .models.SignUpPreference import SignUpPreference
from .models.SkillLevel import SkillLevel
from .models.SortedRoom import SortedRoom
from .models.Team import Team
from .models.VPIPreference import VPIPreference
from .permissions import IsStaffOrTargetUser
from .serializers import RoomSerializer, TeamSerializer, JudgeSerializer, SortedRoomSerializer, \
    VPIPreferenceSerializer, SignUpPreferenceSerializer, MemberSerializer, DebaterPreferenceSerializer, \
    SkillLevelSerializer, UserSerializer


class RoomCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)

    def perform_create(self, serializer):
        """Save the post data when creating a new room."""
        serializer.save()


class RoomDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)


class TeamCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)

    def perform_create(self, serializer):
        """Save the post data when creating a new room."""
        serializer.save()


class TeamDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)


class JudgeCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Judge.objects.all()
    serializer_class = JudgeSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)

    def perform_create(self, serializer):
        """Save the post data when creating a new room."""
        serializer.save()


class JudgeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Judge.objects.all()
    serializer_class = JudgeSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)


class SortedRoomCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = SortedRoom.objects.all()
    serializer_class = SortedRoomSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)

    def perform_create(self, serializer):
        """Save the post data when creating a new room."""
        serializer.save()


class SortedRoomDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    # import pdb
    # pdb.set_trace()

    queryset = SortedRoom.objects.all()
    serializer_class = SortedRoomSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)


class VPIPreferenceCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = VPIPreference.objects.all()
    serializer_class = VPIPreferenceSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)

    def perform_create(self, serializer):
        """Save the post data when creating a new room."""
        serializer.save()


class VPIPreferenceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = VPIPreference.objects.all()
    serializer_class = VPIPreferenceSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)


class SignUpPreferenceCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = SignUpPreference.objects.all()
    serializer_class = SignUpPreferenceSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)

    def perform_create(self, serializer):
        """Save the post data when creating a new room."""
        serializer.save()


class SignUpPreferenceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = SignUpPreference.objects.all()
    serializer_class = SignUpPreferenceSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)


class MemberCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)

    def perform_create(self, serializer):
        """Save the post data when creating a new room."""
        serializer.save()


class MemberDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)


class DebaterPreferenceCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DebaterPreference.objects.all()
    serializer_class = DebaterPreferenceSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)

    def perform_create(self, serializer):
        """Save the post data when creating a new room."""
        serializer.save()


class DebaterPreferenceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = DebaterPreference.objects.all()
    serializer_class = DebaterPreferenceSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)


class SkillLevelCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = SkillLevel.objects.all()
    serializer_class = SkillLevelSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)

    def perform_create(self, serializer):
        """Save the post data when creating a new room."""
        serializer.save()


class SkillLevelDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""
    queryset = SkillLevel.objects.all()
    serializer_class = SkillLevelSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User
    authentication_classes = (TokenAuthentication, BasicAuthentication)

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),