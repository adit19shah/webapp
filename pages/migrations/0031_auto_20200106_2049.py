# Generated by Django 3.0 on 2020-01-06 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0030_auto_20200106_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='itime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 20, 49, 56, 637198)),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='otime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 20, 49, 56, 638197)),
        ),
        migrations.AlterField(
            model_name='exit',
            name='otime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 20, 49, 56, 639196)),
        ),
        migrations.AlterField(
            model_name='host',
            name='itime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 20, 49, 56, 635199)),
        ),
    ]
