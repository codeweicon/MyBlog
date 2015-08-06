# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_auto_20150718_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='datetime',
            field=models.DateField(max_length=20),
        ),
    ]
