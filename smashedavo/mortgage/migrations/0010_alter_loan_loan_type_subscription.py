# Generated by Django 4.2.13 on 2024-05-27 15:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mortgage', '0009_loan_delete_mortgage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_type',
            field=models.CharField(choices=[('MTG', 'Mortgage'), ('HEQ', 'Home Equity'), ('CAR', 'Car'), ('PSL', 'Personal'), ('STD', 'Student'), ('OTH', 'Other')], default='MTG', max_length=3),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=50)),
                ('interval', models.CharField(choices=[('WK', 'Weekly'), ('FT', 'Fortnightly'), ('MT', 'Monthly'), ('AN', 'Annual')], default='MT', max_length=2)),
                ('category', models.CharField(choices=[('STR', 'Streaming'), ('GAM', 'Gaming'), ('ECM', 'Ecommerce'), ('SFT', 'Software'), ('LRN', 'Learning'), ('NWS', 'News'), ('OTH', 'Other')], default='OTH', max_length=3)),
                ('start_date', models.DateField(default=datetime.datetime(2024, 5, 27, 15, 58, 4, 752724, tzinfo=datetime.timezone.utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]