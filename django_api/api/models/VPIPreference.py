from django.db import models


class VPIPreference(models.Model):
    judgeless_rooms = models.BooleanField(default=False)
    room_type = (
        ('NOV', 'NOV'),
        ('PRO', 'PRO'),
        ('ADVANCED', 'ADVANCED'),
        ('PROAM', 'PROAM'),
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
