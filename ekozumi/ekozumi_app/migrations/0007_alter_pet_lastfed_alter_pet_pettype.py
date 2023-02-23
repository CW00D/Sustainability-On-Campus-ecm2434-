# Generated by Django 4.1.5 on 2023-02-23 11:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekozumi_app', '0006_alter_pet_lastfed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='lastFed',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 11, 20, 10, 345733, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='pet',
            name='petType',
            field=models.CharField(choices=[('Hedgehog', 'Hedgehog'), ('Badger', 'Badger'), ('Frog', 'Frog'), ('Bat', 'Bat'), ('Weasel', 'Weasel'), ('Rabbit', 'Rabbit')], max_length=9),
        ),
    ]