from django.db import models
from .Member import Member


class Team(models.Model):
    debater_one_id = models.ForeignKey('Member')
    debater_two_id = models.ForeignKey('Member')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    skill_level = (
        ('NOV', 'NOV'),
        ('PRO', 'PRO'),
        ('ADVANCED', 'ADVANCED'),
        ('PROAM', 'PROAM'),
    )
