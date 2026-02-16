from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Games(models.Model):
    active = models.BooleanField

class GameEngines(models.Model):
    AGENT_CHOICES =[
        ('RANDOM', 'random agent'),
        ('MINMAX', 'minmax agent')
    ]
    engine_name = models.CharField(choices=AGENT_CHOICES)
    difficulty = models.IntegerField(default=1)