from django.db import models
from .Team import Team
from .Room import Room
from .SkillLevel import SkillLevel


class SortedRoom(models.Model):
    og_id = models.ForeignKey(Team, related_name='OG')
    oo_id = models.ForeignKey(Team, related_name='OO')
    cg_id = models.ForeignKey(Team, related_name='CG')
    co_id = models.ForeignKey(Team, related_name='CO')
    room_id = models.ForeignKey(Room)
    skill_level = models.ForeignKey(SkillLevel)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
