# Generated by Django 4.2.11 on 2024-03-25 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpl', '0013_alter_player_chance_of_playing_next_round'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='corners_and_indirect_freekicks_order',
            field=models.IntegerField(null=True),
        ),
    ]
