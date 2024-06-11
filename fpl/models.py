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

    def __str__(self):
        return self.name


class Event(models.Model):
    fpl_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Fixture(models.Model):
    fpl_id = models.IntegerField(unique=True)
    team_h = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_h')
    team_a = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_a')
    team_h_difficulty = models.IntegerField(null=True)
    team_a_difficulty = models.IntegerField(null=True)
    team_h_score = models.IntegerField(null=True)
    team_a_score = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.team_h} vs {self.team_a} ({self.id})"


class Player(models.Model):
    second_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    fpl_id = models.IntegerField(unique=True)
    team = models.ForeignKey(to=Team, on_delete=models.CASCADE)
    element_type = models.CharField(max_length=30,
                                    choices=[(1, 'Goalkeeper'), (2, 'Defender'), (3, 'Midfielder'), (4, 'Forward')])
    total_points = models.IntegerField()
    points_per_game = models.FloatField()
    chance_of_playing_next_round = models.FloatField(null=True)
    ep_next = models.FloatField()
    form = models.FloatField()
    now_cost = models.IntegerField()
    minutes = models.IntegerField()
    goals_scored = models.IntegerField()
    assists = models.IntegerField()
    clean_sheets = models.IntegerField()
    goals_conceded = models.IntegerField()
    own_goals = models.IntegerField()
    penalties_saved = models.IntegerField()
    penalties_missed = models.IntegerField()
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()
    saves = models.IntegerField()
    bonus = models.IntegerField()
    bps = models.IntegerField()
    influence = models.FloatField()
    creativity = models.FloatField()
    threat = models.FloatField()
    ict_index = models.FloatField()
    starts = models.IntegerField()
    expected_goals = models.FloatField()
    expected_assists = models.FloatField()
    expected_goal_involvements = models.FloatField()
    expected_goals_conceded = models.FloatField()
    influence_rank = models.IntegerField()
    influence_rank_type = models.CharField(max_length=255)
    creativity_rank = models.IntegerField()
    creativity_rank_type = models.CharField(max_length=255)
    threat_rank = models.IntegerField()
    threat_rank_type = models.CharField(max_length=255)
    ict_index_rank = models.IntegerField()
    ict_index_rank_type = models.CharField(max_length=255)
    corners_and_indirect_freekicks_order = models.IntegerField(null=True)
    direct_freekicks_order = models.IntegerField(null=True)
    penalties_order = models.IntegerField(null=True)
    expected_goals_per_90 = models.FloatField()
    saves_per_90 = models.FloatField()
    expected_assists_per_90 = models.FloatField()
    expected_goal_involvements_per_90 = models.FloatField()
    expected_goals_conceded_per_90 = models.FloatField()
    goals_conceded_per_90 = models.FloatField()
    form_rank = models.IntegerField()
    form_rank_type = models.CharField(max_length=255)
    points_per_game_rank = models.IntegerField()
    points_per_game_rank_type = models.CharField(max_length=255)
    selected_rank = models.IntegerField()
    selected_rank_type = models.CharField(max_length=255)
    starts_per_90 = models.FloatField()
    clean_sheets_per_90 = models.FloatField()

    def __str__(self):
        return f"{self.first_name} {self.second_name} ({self.id})"


class PointsInFixture(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE)
    predicted_points = models.IntegerField()
    actual_points = models.IntegerField()

    class Meta:
        unique_together = [["player", "fixture"]]


class FPLManager(models.Model):
    fpl_manager_id = models.IntegerField()
    players = models.ManyToManyField(Player, blank=True)

    def give_me_list_of_my_players(self):
        return [player for player in self.players.all()]

    def __str__(self):
        return str(self.fpl_manager_id)


class OverallStatistics(models.Model):
    gameweek = models.CharField(max_length=30)
    average_score = models.IntegerField()
    transfers_made = models.IntegerField()

    def __str__(self):
        return str(self.gameweek)
