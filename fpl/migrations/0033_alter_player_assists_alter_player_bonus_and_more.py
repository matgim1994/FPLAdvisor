# Generated by Django 4.2.11 on 2024-04-19 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpl', '0032_alter_event_fpl_id_alter_fixture_fpl_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='assists',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='bonus',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='bps',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='chance_of_playing_next_round',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='clean_sheets',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='clean_sheets_per_90',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='corners_and_indirect_freekicks_order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='creativity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='creativity_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='creativity_rank_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='direct_freekicks_order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='ep_next',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='expected_assists',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='expected_assists_per_90',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='expected_goal_involvements',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='expected_goal_involvements_per_90',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='expected_goals',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='expected_goals_conceded',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='expected_goals_conceded_per_90',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='expected_goals_per_90',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='form',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='form_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='form_rank_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='goals_conceded',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='goals_conceded_per_90',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='goals_scored',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='ict_index',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='ict_index_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='ict_index_rank_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='influence',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='influence_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='influence_rank_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='minutes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='now_cost',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='own_goals',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='penalties_missed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='penalties_order',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='penalties_saved',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='points_per_game',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='points_per_game_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='points_per_game_rank_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='red_cards',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='saves',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='saves_per_90',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='selected_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='selected_rank_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='starts',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='starts_per_90',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='threat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='threat_rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='threat_rank_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='total_points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='yellow_cards',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]