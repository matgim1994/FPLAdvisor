# Generated by Django 4.2.11 on 2024-03-30 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpl', '0023_rename_fpl_id_fixture_fixture_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='team_a_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fixture',
            name='team_h_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]