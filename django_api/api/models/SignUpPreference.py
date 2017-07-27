from django.db import models
from .Member import Member
from .DebaterPreference import DebaterPreference


class SignUpPreference(models.Model):
    member_id = models.ForeignKey(Member, default=None)
    name = models.CharField(max_length=255, blank=False, unique=True)
    partner_preference = models.ForeignKey(Member, default=None)
    debater_preference = models.ForeignKey(DebaterPreference)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
