from django.db import models
from .Member import Member


class SignUpPreference(models.Model):
    member_id = models.ForeignKey(Member, default=None)  # defaults to None
    name = models.CharField(max_length=255, blank=False, unique=True)
    partner_preference = models.ForeignKey('Member')
    # DEBATER_PREFERENCE_CHOICES = (
    #     ('DEBATE', 'DEBATE'),
    #     ('JUDGE', 'JUDGE'),
    #     ('DEBATE_OR_JUDGE', 'DEBATE_OR_JUDGE'),
    # )
    # debater_preference = models.CharField(choices=DEBATER_PREFERENCE_CHOICES, default='DEBATE')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
