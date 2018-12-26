# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='uaddr',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uemai',
            field=models.CharField(max_length=30, default=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uname',
            field=models.CharField(max_length=20, default=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uphone',
            field=models.CharField(max_length=11, default=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='upost',
            field=models.CharField(max_length=6, default=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='upwd',
            field=models.CharField(max_length=40, default=''),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='urecv',
            field=models.CharField(max_length=20, default=''),
        ),
    ]
