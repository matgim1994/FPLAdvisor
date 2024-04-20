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
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
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
    total_points = models.IntegerField(blank=True, null=True)
    points_per_game = models.FloatField(blank=True, null=True)
    chance_of_playing_next_round = models.FloatField(blank=True, null=True)
    ep_next = models.FloatField(blank=True, null=True)
    form = models.FloatField(blank=True, null=True)
    now_cost = models.IntegerField(blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    goals_scored = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    clean_sheets = models.IntegerField(blank=True, null=True)
    goals_conceded = models.IntegerField(blank=True, null=True)
    own_goals = models.IntegerField(blank=True, null=True)
    penalties_saved = models.IntegerField(blank=True, null=True)
    penalties_missed = models.IntegerField(blank=True, null=True)
    yellow_cards = models.IntegerField(blank=True, null=True)
    red_cards = models.IntegerField(blank=True, null=True)
    saves = models.IntegerField(blank=True, null=True)
    bonus = models.IntegerField(blank=True, null=True)
    bps = models.IntegerField(blank=True, null=True)
    influence = models.FloatField(blank=True, null=True)
    creativity = models.FloatField(blank=True, null=True)
    threat = models.FloatField(blank=True, null=True)
    ict_index = models.FloatField(blank=True, null=True)
    starts = models.IntegerField(blank=True, null=True)
    expected_goals = models.FloatField(blank=True, null=True)
    expected_assists = models.FloatField(blank=True, null=True)
    expected_goal_involvements = models.FloatField(blank=True, null=True)
    expected_goals_conceded = models.FloatField(blank=True, null=True)
    influence_rank = models.IntegerField(blank=True, null=True)
    influence_rank_type = models.CharField(max_length=255, blank=True, null=True)
    creativity_rank = models.IntegerField(blank=True, null=True)
    creativity_rank_type = models.CharField(max_length=255, blank=True, null=True)
    threat_rank = models.IntegerField(blank=True, null=True)
    threat_rank_type = models.CharField(max_length=255, blank=True, null=True)
    ict_index_rank = models.IntegerField(blank=True, null=True)
    ict_index_rank_type = models.CharField(max_length=255, blank=True, null=True)
    corners_and_indirect_freekicks_order = models.IntegerField(blank=True, null=True)
    direct_freekicks_order = models.IntegerField(blank=True, null=True)
    penalties_order = models.IntegerField(blank=True, null=True)
    expected_goals_per_90 = models.FloatField(blank=True, null=True)
    saves_per_90 = models.FloatField(blank=True, null=True)
    expected_assists_per_90 = models.FloatField(blank=True, null=True)
    expected_goal_involvements_per_90 = models.FloatField(blank=True, null=True)
    expected_goals_conceded_per_90 = models.FloatField(blank=True, null=True)
    goals_conceded_per_90 = models.FloatField(blank=True, null=True)
    form_rank = models.IntegerField(blank=True, null=True)
    form_rank_type = models.CharField(max_length=255, blank=True, null=True)
    points_per_game_rank = models.IntegerField(blank=True, null=True)
    points_per_game_rank_type = models.CharField(max_length=255, blank=True, null=True)
    selected_rank = models.IntegerField(blank=True, null=True)
    selected_rank_type = models.CharField(max_length=255, blank=True, null=True)
    starts_per_90 = models.FloatField(blank=True, null=True)
    clean_sheets_per_90 = models.FloatField(blank=True, null=True)


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
