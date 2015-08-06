# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20150718_0131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='datatime',
            new_name='datetime',
        ),
    ]
