# Generated by Django 3.2 on 2023-11-12 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('current_club', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player_Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=100)),
                ('competition', models.CharField(max_length=100)),
                ('goals', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('games', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('draws', models.IntegerField()),
                ('defeats', models.IntegerField()),
                ('team_goals', models.IntegerField()),
                ('minutes_played', models.IntegerField()),
                ('season', models.CharField(max_length=100)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.players')),
            ],
        ),
    ]
