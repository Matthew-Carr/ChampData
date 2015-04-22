# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChampData', '0002_auto_20150415_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='champion',
            name='asPlus',
            field=models.DecimalField(default=0, verbose_name=b'attack speed per level', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='champion',
            name='aSpeed',
            field=models.DecimalField(default=0, verbose_name=b'attack speed', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='champion',
            name='ad',
            field=models.DecimalField(default=0, verbose_name=b'attack damage', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='champion',
            name='adPlus',
            field=models.DecimalField(default=0, verbose_name=b'attack damage per level', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='champion',
            name='ar',
            field=models.DecimalField(default=0, verbose_name=b'armor', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='champion',
            name='arPlus',
            field=models.DecimalField(default=0, verbose_name=b'armor per level', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='champion',
            name='hp',
            field=models.DecimalField(default=0, verbose_name=b'health', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='champion',
            name='hp5',
            field=models.DecimalField(default=0, verbose_name=b'health per 5', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='champion',
            name='hp5Plus',
            field=models.DecimalField(default=0, verbose_name=b'health per 5 per level', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='champion',
            name='hpPlus',
            field=models.DecimalField(default=0, verbose_name=b'health per level', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='champion',
            name='mp',
            field=models.DecimalField(default=0, verbose_name=b'mana', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='champion',
            name='mp5',
            field=models.DecimalField(default=0, verbose_name=b'mana per 5', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='champion',
            name='mp5Plus',
            field=models.DecimalField(default=0, verbose_name=b'mana per 5 per level', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='champion',
            name='mpPlus',
            field=models.DecimalField(default=0, verbose_name=b'mana per level', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='champion',
            name='mr',
            field=models.DecimalField(default=0, verbose_name=b'magic resist', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='champion',
            name='mrPlus',
            field=models.DecimalField(default=0, verbose_name=b'magic resist per level', max_digits=6, decimal_places=3),
        ),
    ]
