from django.contrib import admin
from .models.Member import Member
from .models.Room import Room
from .models.SortedRoom import SortedRoom
from .models.VPIPreference import VPIPreference
from .models.DebaterPreference import DebaterPreference
from .models.Judge import Judge
from .models.SignUpPreference import SignUpPreference
from .models.SkillLevel import SkillLevel
from .models.Team import Team


# Register your models here.
@admin.register(Member, Room, SortedRoom, VPIPreference, DebaterPreference, Judge, SignUpPreference, SkillLevel, Team)
class Exec(admin.ModelAdmin):
    pass
