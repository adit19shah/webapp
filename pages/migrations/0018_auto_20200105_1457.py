# Generated by Django 3.0 on 2020-01-05 09:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20200105_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='itime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 5, 9, 27, 57, 821978, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='otime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 5, 9, 27, 57, 822977, tzinfo=utc)),
        ),
        migrations.AlterModelTable(
            name='host',
            table='host',
        ),
    ]