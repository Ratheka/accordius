# Generated by Django 2.1.1 on 2018-09-13 02:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lw2', '0013_auto_20180913_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='curated_date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='frontpage_date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='voted_at',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]
