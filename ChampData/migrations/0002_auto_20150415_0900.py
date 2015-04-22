# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChampData', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='champion',
            name='aSpeed',
            field=models.IntegerField(default=0, verbose_name=b'attack speed'),
        ),
        migrations.AddField(
            model_name='champion',
            name='ad',
            field=models.IntegerField(default=0, verbose_name=b'attack damage'),
        ),
        migrations.AddField(
            model_name='champion',
            name='adPlus',
            field=models.IntegerField(default=0, verbose_name=b'attack damage per level'),
        ),
        migrations.AddField(
            model_name='champion',
            name='adRange',
            field=models.IntegerField(default=0, verbose_name=b'range'),
        ),
        migrations.AddField(
            model_name='champion',
            name='ar',
            field=models.IntegerField(default=0, verbose_name=b'armor'),
        ),
        migrations.AddField(
            model_name='champion',
            name='arPlus',
            field=models.IntegerField(default=0, verbose_name=b'armor per level'),
        ),
        migrations.AddField(
            model_name='champion',
            name='hp',
            field=models.IntegerField(default=0, verbose_name=b'health'),
        ),
        migrations.AddField(
            model_name='champion',
            name='hp5',
            field=models.IntegerField(default=0, verbose_name=b'health per 5'),
        ),
        migrations.AddField(
            model_name='champion',
            name='hp5Plus',
            field=models.IntegerField(default=0, verbose_name=b'health per 5 per level'),
        ),
        migrations.AddField(
            model_name='champion',
            name='hpPlus',
            field=models.IntegerField(default=0, verbose_name=b'health per level'),
        ),
        migrations.AddField(
            model_name='champion',
            name='mp',
            field=models.IntegerField(default=0, verbose_name=b'mana'),
        ),
        migrations.AddField(
            model_name='champion',
            name='mp5',
            field=models.IntegerField(default=0, verbose_name=b'mana per 5'),
        ),
        migrations.AddField(
            model_name='champion',
            name='mp5Plus',
            field=models.IntegerField(default=0, verbose_name=b'mana per 5 per level'),
        ),
        migrations.AddField(
            model_name='champion',
            name='mpPlus',
            field=models.IntegerField(default=0, verbose_name=b'mana per level'),
        ),
        migrations.AddField(
            model_name='champion',
            name='mr',
            field=models.IntegerField(default=0, verbose_name=b'magic resist'),
        ),
        migrations.AddField(
            model_name='champion',
            name='mrPlus',
            field=models.IntegerField(default=0, verbose_name=b'magic resist per level'),
        ),
        migrations.AddField(
            model_name='champion',
            name='ms',
            field=models.IntegerField(default=0, verbose_name=b'movement speed'),
        ),
    ]
