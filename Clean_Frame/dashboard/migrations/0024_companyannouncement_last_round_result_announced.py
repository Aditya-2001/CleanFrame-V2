# Generated by Django 2.2.19 on 2021-03-21 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_internshipfinalresult_student_agrees'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyannouncement',
            name='last_round_result_announced',
            field=models.BooleanField(default=False),
        ),
    ]
