from django.db import models
from .Member import Member
from .SkillLevel import SkillLevel


class Team(models.Model):
    debater_one_id = models.ForeignKey(Member, related_name='debater_one')
    debater_two_id = models.ForeignKey(Member, related_name='debater_two')
    skill_level = models.ForeignKey(SkillLevel)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.debater_one_id.user.username + '/' + self.debater_two_id.user.username + ', ' + \
               self.date_created.strftime('%x')
