from django.db import models
from .Member import Member
from .DebaterPreference import DebaterPreference


class SignUpPreference(models.Model):
    member_id = models.ForeignKey(Member, default=None)
    partner_preference = models.ForeignKey(Member, default=None, related_name='partner')
    debater_preference = models.ForeignKey(DebaterPreference)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.member_id.user.username + ': ' + self.debater_preference.name + ', ' + \
               self.date_created.strftime('%x')
