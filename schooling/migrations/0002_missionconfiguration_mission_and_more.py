# Generated by Django 5.0.1 on 2024-05-18 02:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_role_user_role'),
        ('schooling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='missionconfiguration',
            name='mission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='mission_conf', to='schooling.mission', verbose_name='Mission '),
        ),
        migrations.AlterField(
            model_name='missionconfiguration',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='school_agent_conf', to='authentication.school', verbose_name='School'),
        ),
    ]