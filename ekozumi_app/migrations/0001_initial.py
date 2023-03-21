# Generated by Django 4.0.2 on 2023-03-21 16:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('userID', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('locationID', models.AutoField(primary_key=True, serialize=False)),
                ('locationName', models.CharField(max_length=50)),
                ('dayOfAppearance', models.DateField(unique=True)),
                ('minLongitude', models.FloatField()),
                ('maxLongitude', models.FloatField()),
                ('minLatitude', models.FloatField()),
                ('maxLatitude', models.FloatField()),
                ('locationHint', models.CharField(max_length=500)),
                ('anagramWord', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Megaboss',
            fields=[
                ('megabossID', models.AutoField(primary_key=True, serialize=False)),
                ('megabossName', models.CharField(max_length=50)),
                ('dayOfAppearance', models.DateField(unique=True)),
                ('megabossImage', models.CharField(max_length=50)),
                ('megabossAngryImage', models.CharField(max_length=50)),
                ('megabossIntroDialogue', models.CharField(max_length=500)),
                ('megabossOutroDialogue', models.CharField(max_length=500)),
                ('megabossQ1', models.CharField(max_length=500)),
                ('megabossQ1CA', models.CharField(max_length=500)),
                ('megabossQ1WA1', models.CharField(max_length=500)),
                ('megabossQ1WA2', models.CharField(max_length=500)),
                ('megabossQ1WA3', models.CharField(max_length=500)),
                ('megabossQ2', models.CharField(max_length=500)),
                ('megabossQ2CA', models.CharField(max_length=500)),
                ('megabossQ2WA1', models.CharField(max_length=500)),
                ('megabossQ2WA2', models.CharField(max_length=500)),
                ('megabossQ2WA3', models.CharField(max_length=500)),
                ('megabossQ3', models.CharField(max_length=500)),
                ('megabossQ3CA', models.CharField(max_length=500)),
                ('megabossQ3WA1', models.CharField(max_length=500)),
                ('megabossQ3WA2', models.CharField(max_length=500)),
                ('megabossQ3WA3', models.CharField(max_length=500)),
                ('megabossQ4', models.CharField(max_length=500)),
                ('megabossQ4CA', models.CharField(max_length=500)),
                ('megabossQ4WA1', models.CharField(max_length=500)),
                ('megabossQ4WA2', models.CharField(max_length=500)),
                ('megabossQ4WA3', models.CharField(max_length=500)),
                ('timesFought', models.IntegerField(default=0)),
                ('averageTime', models.IntegerField(default=0)),
                ('averageAttempts', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('monsterID', models.AutoField(primary_key=True, serialize=False)),
                ('monsterName', models.CharField(max_length=50)),
                ('dayOfAppearance', models.DateField(unique=True)),
                ('monsterImage', models.CharField(max_length=50)),
                ('monsterAngryImage', models.CharField(max_length=50)),
                ('monsterIntroDialogue', models.CharField(max_length=500)),
                ('playerIntroDialogue', models.CharField(max_length=500)),
                ('monsterOutroDialogue', models.CharField(max_length=500)),
                ('playerOutroDialogue', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('petID', models.AutoField(primary_key=True, serialize=False)),
                ('petName', models.CharField(max_length=50)),
                ('lastFed', models.DateTimeField(default=datetime.datetime(2023, 3, 20, 16, 25, 47, 892503, tzinfo=utc))),
                ('petType', models.CharField(choices=[('Hedgehog', 'Hedgehog'), ('Fox', 'Fox'), ('Frog', 'Frog'), ('Rabbit', 'Rabbit'), ('Bluetit', 'Bluetit')], max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('petID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ekozumi_app.pet')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
