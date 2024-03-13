from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=50)


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
