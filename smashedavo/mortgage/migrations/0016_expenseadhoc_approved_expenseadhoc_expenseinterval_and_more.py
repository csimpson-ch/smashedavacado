# Generated by Django 4.2.13 on 2024-05-29 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mortgage', '0015_rename_start_date_expenseinterval_next_payment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenseadhoc',
            name='approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='expenseadhoc',
            name='expenseinterval',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mortgage.expenseinterval'),
        ),
        migrations.AddField(
            model_name='expenseadhoc',
            name='loan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mortgage.loan'),
        ),
    ]