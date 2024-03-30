# Generated by Django 4.2.11 on 2024-03-29 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fpl', '0015_alter_player_direct_freekicks_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fplmanager',
            name='players',
            field=models.ManyToManyField(blank=True, to='fpl.player'),
        ),
        migrations.CreateModel(
            name='PointsInFixture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predicted_points', models.FloatField()),
                ('actual_points', models.FloatField()),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fpl.fixture')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fpl.player')),
            ],
        ),
    ]