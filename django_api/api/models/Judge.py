from django.db import models
from .Member import Member
from .SortedRoom import SortedRoom


# Says that Member and SortedRoom import statements are not used
class Judge(models.Model):
    member_id = models.ForeignKey('Member')
    sorted_room_id = models.ForeignKey('SortedRoom')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
