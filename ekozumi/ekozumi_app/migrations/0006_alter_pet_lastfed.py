# Generated by Django 4.1.5 on 2023-02-22 12:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ekozumi_app', '0005_pet_pettype_alter_pet_lastfed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='lastFed',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
