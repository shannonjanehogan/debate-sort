from django.contrib.auth.models import User
from rest_framework import serializers
from .models.Room import Room
from .models.Judge import Judge
from .models.Team import Team
from .models.SortedRoom import SortedRoom
from .models.VPIPreference import VPIPreference
from .models.Member import Member
from .models.SignUpPreference import SignUpPreference
from .models.DebaterPreference import DebaterPreference
from .models.SkillLevel import SkillLevel


class RoomSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Room
        fields = ['id', 'name', 'date_created', 'date_modified']
        read_only_fields = ['date_created', 'date_modified']


class JudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = ['id', 'member_id', 'sorted_room_id', 'date_created', 'date_modified']
        read_only_fields = ['date_created', 'date_modified']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'debater_one_id', 'debater_two_id', 'skill_level', 'date_created', 'date_modified']
        read_only_fields = ['date_created', 'date_modified']


class SortedRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = SortedRoom
        fields = ['id', 'og_id', 'oo_id', 'cg_id', 'co_id', 'room_id', 'skill_level', 'date_created', 'date_modified']
        read_only_fields = ['date_created', 'date_modified']


class SignUpPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUpPreference
        fields = ['id', 'member_id', 'partner_preference', 'debate_preference', 'date_created', 'date_modified']
        read_only_fields = ['date_created', 'date_modified']


class VPIPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VPIPreference
        fields = ['id', 'judgeless_rooms', 'room_type', 'date_created', 'date_modified']
        read_only_fields = ['date_created', 'date_modified']


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'skill_level']


class DebaterPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebaterPreference
        fields = ['id', 'debater_preference', 'date_created', 'date_modified']
        read_only_fields = ['date_created', 'date_modified']


class SkillLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillLevel
        fields = ['id', 'skill_level', 'date_created', 'date_modified']
        read_only_fields = ['date_created', 'date_modified']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'email',)
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    def restore_object(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user
