# Generated by Django 4.2.11 on 2024-03-25 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpl', '0012_player_assists_player_bonus_player_bps_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='chance_of_playing_next_round',
            field=models.FloatField(null=True),
        ),
    ]
