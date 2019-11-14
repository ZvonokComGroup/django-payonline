# Generated by Django 2.2.2 on 2019-11-14 13:51

from django.db import migrations, models
import payonline.fields.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', payonline.fields.models.UTCDateTimeField()),
                ('transaction_id', models.BigIntegerField()),
                ('order_id', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=14)),
                ('currency', models.CharField(choices=[('RUB', 'RUB'), ('USD', 'USD'), ('EUR', 'EUR')], max_length=3)),
                ('payment_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True)),
                ('payment_currency', models.CharField(blank=True, choices=[('RUB', 'RUB'), ('USD', 'USD'), ('EUR', 'EUR')], max_length=3, null=True)),
                ('card_holder', models.CharField(blank=True, max_length=255)),
                ('card_number', models.CharField(blank=True, max_length=16)),
                ('country', models.CharField(blank=True, max_length=2, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('ip_address', models.CharField(blank=True, max_length=255, null=True)),
                ('ip_country', models.CharField(blank=True, max_length=10, null=True)),
                ('bin_country', models.CharField(blank=True, max_length=10, null=True)),
                ('special_conditions', models.CharField(blank=True, max_length=255, null=True)),
                ('provider', models.CharField(blank=True, max_length=32, null=True)),
                ('rebill_anchor', models.CharField(blank=True, max_length=32, null=True)),
                ('fiscal_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
