from django.contrib import admin
from .models.Member import Member
from .models.Room import Room
from .models.SortedRoom import SortedRoom
from .models.VPIPreference import VPIPreference


# Register your models here.
@admin.register(Member, Room, SortedRoom, VPIPreference)
class Exec(admin.ModelAdmin):
    pass
