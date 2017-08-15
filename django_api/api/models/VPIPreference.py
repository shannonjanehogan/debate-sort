from django.db import models
from .SkillLevel import SkillLevel


class VPIPreference(models.Model):
    judgeless_rooms = models.BooleanField(default=False)
    room_type = models.ForeignKey(SkillLevel)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.date_created.strftime('%x')
