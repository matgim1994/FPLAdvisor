# Generated by Django 4.2.11 on 2024-03-24 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fpl', '0003_fplmanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fpl_id', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fpl.event')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('fpl_id', models.IntegerField(unique=True)),
                ('strength', models.IntegerField()),
                ('strength_overall_home', models.IntegerField()),
                ('strength_overall_away', models.IntegerField()),
                ('strength_attack_home', models.IntegerField()),
                ('strength_attack_away', models.IntegerField()),
                ('strength_defence_home', models.IntegerField()),
                ('strength_defence_away', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='player',
            name='club',
        ),
        migrations.AddField(
            model_name='fplmanager',
            name='players',
            field=models.ManyToManyField(to='fpl.player'),
        ),
        migrations.AddField(
            model_name='player',
            name='element_type',
            field=models.CharField(choices=[(1, 'Goalkeeper'), (2, 'Defender'), (3, 'Midfielder'), (4, 'Forward')], default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='ep_next',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='form',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='now_cost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Club',
        ),
        migrations.AddField(
            model_name='fixture',
            name='team_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_a', to='fpl.team'),
        ),
        migrations.AddField(
            model_name='fixture',
            name='team_h',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_h', to='fpl.team'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fpl.team'),
            preserve_default=False,
        ),
    ]
