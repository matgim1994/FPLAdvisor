# Generated by Django 4.2.11 on 2024-03-30 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpl', '0021_alter_player_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='team_a_team_h_difficulty',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fixture',
            name='team_h_difficulty',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
