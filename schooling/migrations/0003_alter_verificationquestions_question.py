# Generated by Django 5.0.1 on 2024-05-18 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schooling', '0002_missionconfiguration_mission_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationquestions',
            name='question',
            field=models.CharField(blank=True, max_length=256, verbose_name='Question'),
        ),
    ]