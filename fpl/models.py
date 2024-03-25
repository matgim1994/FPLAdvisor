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
    second_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    player_id = models.IntegerField(unique=True)
    club = models.CharField(max_length=255)
    element_type = models.CharField(max_length=30, choices=[(1, 'Goalkeeper'), (2, 'Defender'), (3, 'Midfielder'), (4, 'Forward')])
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
