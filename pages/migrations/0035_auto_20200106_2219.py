# Generated by Django 3.0 on 2020-01-06 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0034_auto_20200106_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='itime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 22, 19, 13, 694550)),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='otime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 22, 19, 13, 694550)),
        ),
        migrations.AlterField(
            model_name='exit',
            name='otime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 22, 19, 13, 698549)),
        ),
        migrations.AlterField(
            model_name='host',
            name='itime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 22, 19, 13, 690550)),
        ),
    ]