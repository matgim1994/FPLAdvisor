# Generated by Django 4.2.11 on 2024-03-30 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpl', '0030_rename_fixture_id_fixture_fpl_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointsinfixture',
            name='actual_points',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pointsinfixture',
            name='predicted_points',
            field=models.IntegerField(),
        ),
    ]