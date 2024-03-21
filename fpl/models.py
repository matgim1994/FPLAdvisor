from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=30)

class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

class OverallStatistics(models.Model):
    gameweek = models.CharField(max_length=30)
    average_score = models.IntegerField()
    transfers_made = models.IntegerField()

    def __str__(self):
        return str(self.gameweek)