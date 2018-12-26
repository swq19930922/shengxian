# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('uemai', models.CharField(max_length=30)),
                ('urecv', models.CharField(max_length=20)),
                ('upost', models.CharField(max_length=6)),
                ('uphone', models.CharField(max_length=11)),
                ('uaddr', models.CharField(max_length=100)),
            ],
        ),
    ]
