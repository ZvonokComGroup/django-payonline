from hashlib import md5

from django import forms
from django.utils.datastructures import SortedDict

from .models import PaymentData
from .helpers import DataProxy


class PaymentDefaultForm(forms.Form):

    MerchantId = forms.IntegerField()
    OrderId = forms.CharField(max_length=50)
    Amount = forms.DecimalField(min_value=0, max_digits=14, decimal_places=2)
    Currency = forms.CharField(max_length=3, min_length=3)
    ValidUntil = forms.DateTimeField(required=False)
    OrderDescription = forms.CharField(max_length=100, required=False)
    SecurityKey = forms.CharField(min_length=32, max_length=32)
    ReturnUrl = forms.CharField(required=False)
    FailUrl = forms.CharField(required=False)


class PaymentDataForm(forms.ModelForm):

    SecurityKey = forms.CharField(min_length=32, max_length=32)

    class Meta:
        model = PaymentData

    def __init__(self, *args, **kwargs):
        self.shop = kwargs.pop('shop')
        self.private_security_key = kwargs.pop('private_security_key')
        kwargs['data'] = DataProxy(kwargs['data'])
        super().__init__(*args, **kwargs)

    def get_security_key_params(self):
        params = SortedDict()
        params['DateTime'] = self.data.get('DateTime', '')
        params['TransactionID'] = self.data.get('TransactionID', '')
        params['OrderId'] = self.data.get('OrderId', '')
        params['Amount'] = self.data.get('Amount', '')
        params['Currency'] = self.data.get('Currency', '')
        params['PrivateSecurityKey'] = self.private_security_key
        return params

    def get_security_key(self):
        params = self.get_security_key_params()
        key = md5('&'.join('='.join(i) for i in params.items())).hexdigest()
        return key

    def clean(self):
        if self.cleaned_data.get('SecurityKey') != self.get_security_key():
            self.add_error('SecurityKey', 'Wrong security key')
        return self.cleaned_data
