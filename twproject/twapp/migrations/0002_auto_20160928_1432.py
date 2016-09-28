# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='tweets',
            field=models.ForeignKey(to='twapp.Tweet', null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='tweet',
            name='tags',
            field=models.ForeignKey(to='twapp.Tag', null=True),
        ),
    ]
