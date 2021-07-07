# Generated by Django 3.1.13 on 2021-07-07 05:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0069_auto_20210707_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyannouncement',
            name='announcement_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 7, 11, 20, 54, 938954)),
        ),
        migrations.AlterField(
            model_name='companyannouncement',
            name='last_date_to_apply',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 7, 11, 20, 54, 938954)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 7, 11, 20, 54, 945940)),
        ),
        migrations.AlterField(
            model_name='session',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 7, 11, 20, 54, 936960)),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='date_of_registrations',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 7, 11, 20, 54, 941947)),
        ),
    ]