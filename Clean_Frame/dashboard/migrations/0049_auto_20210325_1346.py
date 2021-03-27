# Generated by Django 2.2.19 on 2021-03-25 13:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0048_auto_20210325_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyannouncement',
            name='announcement_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 13, 46, 35, 985697)),
        ),
        migrations.AlterField(
            model_name='companyannouncement',
            name='last_date_to_apply',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 13, 46, 35, 985675)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 13, 46, 35, 989641)),
        ),
        migrations.AlterField(
            model_name='profilevisibilty',
            name='to_all',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='date_of_registrations',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 25, 13, 46, 35, 987022)),
        ),
    ]