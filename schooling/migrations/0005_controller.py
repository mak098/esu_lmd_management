# Generated by Django 5.0.1 on 2024-05-18 12:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schooling', '0004_finalist'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Controller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(blank=True, default='-', max_length=256, null=True, verbose_name='Response')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('controller_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='controller_by', to=settings.AUTH_USER_MODEL, verbose_name='controller by')),
                ('finalist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='controller_finalist', to='schooling.finalist', verbose_name='Question')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='controller_question', to='schooling.verificationquestions', verbose_name='Question')),
            ],
            options={
                'verbose_name_plural': 'Controllers',
                'db_table': 'controllers',
            },
        ),
    ]
