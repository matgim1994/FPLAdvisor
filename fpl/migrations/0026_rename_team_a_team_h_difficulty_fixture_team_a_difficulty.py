# Generated by Django 4.2.11 on 2024-03-30 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fpl', '0025_remove_fixture_event_alter_fixture_team_a_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fixture',
            old_name='team_a_team_h_difficulty',
            new_name='team_a_difficulty',
        ),
    ]
