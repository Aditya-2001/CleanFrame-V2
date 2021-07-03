# Generated by Django 3.1.13 on 2021-07-02 16:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0057_auto_20210503_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyannouncement',
            name='announcement_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 2, 22, 16, 12, 652455)),
        ),
        migrations.AlterField(
            model_name='companyannouncement',
            name='last_date_to_apply',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 2, 22, 16, 12, 652455)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 2, 22, 16, 12, 659994)),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='date_of_registrations',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 2, 22, 16, 12, 652455)),
        ),
    ]