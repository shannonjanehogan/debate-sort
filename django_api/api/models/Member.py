from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django import forms
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

class Member(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    skill_level = (
        ('NOV', 'NOV'),
        ('PRO', 'PRO'),
        ('ADVANCED', 'ADVANCED'),
    )

# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
