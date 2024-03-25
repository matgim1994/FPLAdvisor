import requests
from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30, unique=True)
    fpl_id = models.IntegerField(unique=True)
    strength = models.IntegerField()
    strength_overall_home = models.IntegerField()
    strength_overall_away = models.IntegerField()
    strength_attack_home = models.IntegerField()
    strength_attack_away = models.IntegerField()
    strength_defence_home = models.IntegerField()
    strength_defence_away = models.IntegerField()


class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    ep_next = models.FloatField()
    element_type = models.CharField(max_length=30, choices=[
        (1, 'Goalkeeper'), (2, 'Defender'), (3, 'Midfielder'), (4, 'Forward')])
    form = models.FloatField()
    now_cost = models.IntegerField()


class Event(models.Model):
    pass


class Fixture(models.Model):
    fpl_id = models.IntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    team_h = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_h')
    team_a = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_a')


class FPLManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    fpl_manager_id = models.IntegerField()
    players = models.ManyToManyField(Player)

    def give_me_list_of_my_players(self):
        return [player for player in self.players.all()]


class OverallStatistics(models.Model):
    gameweek = models.CharField(max_length=30)
    average_score = models.IntegerField()
    transfers_made = models.IntegerField()

    def __str__(self):
        return str(self.gameweek)
