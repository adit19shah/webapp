# Generated by Django 3.0 on 2020-01-04 18:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20200104_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='itime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 4, 18, 26, 25, 847405, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='otime',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 4, 18, 26, 25, 847405, tzinfo=utc)),
        ),
    ]
