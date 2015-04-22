# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChampData', '0003_auto_20150416_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='champion',
            name='asPlus',
            field=models.DecimalField(default=0, verbose_name=b'attack speed per level', max_digits=6, decimal_places=1),
        ),
    ]
