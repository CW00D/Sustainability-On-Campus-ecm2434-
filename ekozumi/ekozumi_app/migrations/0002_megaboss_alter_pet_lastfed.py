# Generated by Django 4.1.5 on 2023-03-19 20:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekozumi_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Megaboss',
            fields=[
                ('megabossID', models.AutoField(primary_key=True, serialize=False)),
                ('megabossName', models.CharField(max_length=50)),
                ('dayOfAppearance', models.DateField(unique=True)),
                ('megabossImage', models.CharField(max_length=50)),
                ('megabossAngryImage', models.CharField(max_length=50)),
                ('megabossIntroDialogue', models.CharField(max_length=500)),
                ('playerIntroDialogue', models.CharField(max_length=500)),
                ('megabossOutroDialogue', models.CharField(max_length=500)),
                ('playerOutroDialogue', models.CharField(max_length=500)),
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
                ('megaboss1CorrectStats', models.IntegerField(default=0)),
                ('megaboss2CorrectStats', models.IntegerField(default=0)),
                ('megaboss3CorrectStats', models.IntegerField(default=0)),
                ('megaboss4CorrectStats', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='pet',
            name='lastFed',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 18, 20, 39, 37, 100666, tzinfo=datetime.timezone.utc)),
        ),
    ]