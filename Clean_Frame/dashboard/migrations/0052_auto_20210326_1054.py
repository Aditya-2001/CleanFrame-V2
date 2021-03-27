# Generated by Django 2.2.19 on 2021-03-26 10:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0051_auto_20210326_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyannouncement',
            name='announcement_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 10, 54, 15, 172427)),
        ),
        migrations.AlterField(
            model_name='companyannouncement',
            name='last_date_to_apply',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 10, 54, 15, 172405)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 10, 54, 15, 175553)),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='date_of_registrations',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 10, 54, 15, 173645)),
        ),
        migrations.CreateModel(
            name='ProfileVisibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_registered_companies', models.BooleanField(default=False)),
                ('to_all_companies', models.BooleanField(default=False)),
                ('to_all_students', models.BooleanField(default=False)),
                ('to_all', models.BooleanField(default=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]