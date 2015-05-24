from django.db import models

# Create your models here.
class Summoner(models.Model):
    summoner_name = models.CharField(max_length=50)
    team_3v3_tier = models.CharField(max_length=10)
    team_3v3_rank = models.CharField(max_length=3)
    team_5v5_tier = models.CharField(max_length=10)
    team_5v5_rank = models.CharField(max_length=3)
    solo_5v5_tier = models.CharField(max_length=10)
    solo_5v5_rank = models.CharField(max_length=3)





