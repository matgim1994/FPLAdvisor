# Generated by Django 4.2.11 on 2024-03-25 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpl', '0014_alter_player_corners_and_indirect_freekicks_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='direct_freekicks_order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='penalties_order',
            field=models.IntegerField(null=True),
        ),
    ]