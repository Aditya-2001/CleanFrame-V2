# Generated by Django 3.1.13 on 2021-07-07 07:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0081_auto_20210707_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyannouncement',
            name='announcement_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 7, 13, 21, 23, 962479)),
        ),
        migrations.AlterField(
            model_name='companyannouncement',
            name='last_date_to_apply',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 7, 13, 21, 23, 962479)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 7, 13, 21, 23, 966459)),
        ),
        migrations.AlterField(
            model_name='session',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 7, 13, 21, 23, 959481)),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='date_of_registrations',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 7, 13, 21, 23, 964429)),
        ),
    ]