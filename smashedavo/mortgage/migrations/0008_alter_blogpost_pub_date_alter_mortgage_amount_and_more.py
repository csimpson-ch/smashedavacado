# Generated by Django 4.2.13 on 2024-05-23 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortgage', '0007_alter_blogpost_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='pub_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='mortgage',
            name='amount',
            field=models.FloatField(default=200000),
        ),
        migrations.AlterField(
            model_name='mortgage',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 5, 23, 16, 14, 44, 205009, tzinfo=datetime.timezone.utc)),
        ),
    ]