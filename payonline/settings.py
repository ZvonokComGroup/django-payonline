from django.conf import settings


CONFIG = {
    'MERCHANT_ID': None,
    'PRIVATE_SECURITY_KEY': None,
    'PAYONLINE_URL': 'https://secure.payonlinesystem.com/ru/payment/select/',
    'FISCAL_URL': 'https://secure.payonlinesystem.com/Services/Fiscal/Request.ashx',
    'SUCCESS_URL': 'https://zvonok.com/manager/payments/payonline/success/',
    'CURRENCY': 'RUB',
}
CONFIG.update(getattr(settings, 'PAYONLINE_CONFIG', {}))
