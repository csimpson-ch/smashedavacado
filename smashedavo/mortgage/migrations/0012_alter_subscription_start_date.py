# Generated by Django 4.2.13 on 2024-05-27 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mortgage', '0011_alter_subscription_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2024, 5, 27, 16, 56, 32, 64188, tzinfo=datetime.timezone.utc)),
        ),
    ]