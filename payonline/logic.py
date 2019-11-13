from hashlib import md5

from .settings import CONFIG


def get_security_key(order_id, amount, merchant_id=CONFIG['MERCHANT_ID'],
                     currency=CONFIG['CURRENCY'],
                     private_security_key=CONFIG['PRIVATE_SECURITY_KEY']):
    params = [('MerchantId', merchant_id),
              ('OrderId', order_id),
              ('Amount', amount),
              ('Currency', currency),
              ('PrivateSecurityKey', private_security_key)]

    return md5('&'.join('='.join(i) for i in params)).hexdigest()
