# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_auto_20150718_0300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='tab',
        ),
        migrations.AlterField(
            model_name='article',
            name='datetime',
            field=models.DateTimeField(max_length=20),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blogapp.Tag', blank=True),
        ),
    ]
