from hashlib import md5

from .settings import CONFIG


def get_security_key(order_id, amount, merchant_id=CONFIG['MERCHANT_ID'],
                     currency=CONFIG['CURRENCY'],
                     private_security_key=CONFIG['PRIVATE_SECURITY_KEY'], valid_until='',
                     order_description=''):
    params = [('MerchantId', str(merchant_id)),
              ('OrderId', str(order_id)),
              ('Amount', str(amount)),
              ('Currency', str(currency))]
    if valid_until:
        params += [('ValidUntil', valid_until)]
    if order_description:
        params += [('OrderDescription', order_description)]
    params += [('PrivateSecurityKey', private_security_key)]

    return md5(('&'.join('='.join(i) for i in params)).encode('utf-8')).hexdigest()
