# Generated by Django 3.1.1 on 2020-10-19 19:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_auto_20201019_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='return_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='borrow_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 22, 23, 27, 37, 947235)),
        ),
    ]