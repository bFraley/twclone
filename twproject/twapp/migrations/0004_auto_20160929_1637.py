# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twapp', '0003_auto_20160928_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='mem',
            new_name='memb',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
