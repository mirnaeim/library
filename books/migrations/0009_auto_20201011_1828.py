# Generated by Django 3.1.1 on 2020-10-11 14:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20201011_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='prof',
            field=models.ImageField(default='images/default/default-profile.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='borrow_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 14, 14, 58, 13, 525341, tzinfo=utc)),
        ),
    ]
