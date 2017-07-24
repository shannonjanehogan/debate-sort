from django.db import models
from .Team import Team
from .Room import Room

class SortedRoom(models.Model):
    og_id = models.ForeignKey('Team')
    oo_id = models.ForeignKey('Team')
    cg_id = models.ForeignKey('Team')
    co_id = models.ForeignKey('Team')
    room_id = models.ForeignKey('Room')
    skill_level = (
        ('NOV', 'NOV'),
        ('PRO', 'PRO'),
        ('ADVANCED', 'ADVANCED'),
        ('PROAM', 'PROAM'),
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
