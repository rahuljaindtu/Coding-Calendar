# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-21 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coding', '0003_upcomingcontest'),
    ]

    operations = [
        migrations.CreateModel(
            name='OngoingContest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=200)),
                ('end_time', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='codechef_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='myuser',
            name='codeforces_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='myuser',
            name='spoj_count',
            field=models.IntegerField(default=0),
        ),
    ]
