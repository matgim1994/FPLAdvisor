# Generated by Django 4.2.11 on 2024-03-25 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpl', '0005_player_player_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='chance_of_playing_next_round',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
