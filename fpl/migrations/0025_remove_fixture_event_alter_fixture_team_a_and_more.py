# Generated by Django 4.2.11 on 2024-03-30 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpl', '0024_fixture_team_a_score_fixture_team_h_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixture',
            name='event',
        ),
        migrations.AlterField(
            model_name='fixture',
            name='team_a',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fixture',
            name='team_h',
            field=models.IntegerField(),
        ),
    ]
