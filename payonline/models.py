from django.db import models
from .fields.models import UTCDateTimeField


class PaymentData(models.Model):

    CURRENCIES = (
        ('RUB', 'RUB'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
    )

    datetime = UTCDateTimeField()
    transaction_id = models.BigIntegerField()
    order_id = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=14, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCIES)
    payment_amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    payment_currency = models.CharField(max_length=3, choices=CURRENCIES, blank=True, null=True)
    card_holder = models.CharField(max_length=255, blank=True)
    card_number = models.CharField(max_length=16, blank=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    ip_address = models.CharField(max_length=255, blank=True, null=True)
    ip_country = models.CharField(max_length=10, blank=True, null=True)
    bin_country = models.CharField(max_length=10, blank=True, null=True)
    special_conditions = models.CharField(max_length=255, blank=True, null=True)
    provider = models.CharField(max_length=32, blank=True, null=True)
    rebill_anchor = models.CharField(max_length=32, blank=True, null=True)


