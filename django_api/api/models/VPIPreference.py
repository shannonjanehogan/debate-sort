from django.db import models


class VPIPreference(models.Model):
    judgeless_rooms = models.BooleanField(default=False)
    # ROOM_TYPE_CHOICES = (
    #     ('NOV', 'NOV'),
    #     ('PRO', 'PRO'),
    #     ('ADVANCED', 'ADVANCED'),
    #     ('PROAM', 'PROAM'),
    # )
    # room_type = models.CharField(choices=ROOM_TYPE_CHOICES, default='NOV')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
