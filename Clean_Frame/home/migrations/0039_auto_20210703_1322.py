# Generated by Django 3.1.13 on 2021-07-03 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_auto_20210703_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='otp_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 13, 22, 19, 711538)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='profile_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 13, 22, 19, 711538)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='signup_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 13, 22, 19, 711538)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='unique_code_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 13, 22, 19, 711538)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='otp_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 13, 22, 19, 710542)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='profile_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 13, 22, 19, 710542)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='signup_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 13, 22, 19, 710542)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='unique_code_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 3, 13, 22, 19, 710542)),
        ),
    ]
