from django.db import models
from .Member import Member


# Says that Member import statements are not used
class SignUpPreference(models.Model):
    member_id = models.ForeignKey('Member')  # this can be null
    name = models.CharField(max_length=255, blank=False, unique=True)
    partner_preference = models.ForeignKey('Member')
    debate_preference = (
        ('DEBATE', 'DEBATE'),
        ('JUDGE', 'JUDGE'),
        ('DEBATE_OR_JUDGE', 'DEBATE_OR_JUDGE'),
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
