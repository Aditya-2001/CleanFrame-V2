# Generated by Django 2.2.19 on 2021-03-13 17:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_auto_20210313_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregistration',
            name='date_of_registrations',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 13, 17, 45, 46, 471538, tzinfo=utc)),
        ),
    ]