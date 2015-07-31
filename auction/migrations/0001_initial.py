# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('team', models.CharField(max_length=3, choices=[(b'MI', b'Mumbai Indians'), (b'DD', b'Delhi Daredevils'), (b'RCB', b'Royal Challengers Bangalore'), (b'KKR', b'Kolkata Knight Riders'), (b'SRH', b'Sunrisers Hyderabad'), (b'RR', b'Rajasthan Royals'), (b'KP', b'Kings XI Punjab')])),
                ('role', models.CharField(max_length=2, choices=[(b'BT', b'Batsman'), (b'BL', b'Bowler'), (b'AR', b'All-rounder')])),
                ('img', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
