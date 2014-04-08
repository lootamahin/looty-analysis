from django.db import models

class Summoner(models.Model):
    username = models.CharField(max_length=200)

class Champion(models.Model):
    name = models.CharField(max_length=200)
