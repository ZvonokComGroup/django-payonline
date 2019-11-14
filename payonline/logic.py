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


def get_good_position(description, quantity, amount, tax):
    return {
        'description': str(description),
        'quantity': quantity,
        'amount': str(amount),
        'tax': tax,
    }


TAX_NO_NDS = 'none'
NDS_20 = 'vat20'


def get_fiscal_data(transaction_id, total_amount, goods, client_inn=None,
                    payment_system_type='card', operation='Benefit'):
    data = {
        'operation': operation,
        'transactionId': transaction_id,
        'paymentSystemType': payment_system_type,
        'totalAmount': total_amount,
        'goods': goods,
    }
    if client_inn:
        data['clientInn'] = client_inn
    return data


def get_fiscal_secret_key(fiscal_body, merchant_id=CONFIG['MERCHANT_ID'],
                          private_security_key=CONFIG['PRIVATE_SECURITY_KEY']):
    params = [('RequestBody', fiscal_body),
              ('MerchantId', str(merchant_id)),
              ('PrivateSecurityKey', private_security_key)]
    return md5(('&'.join('='.join(i) for i in params)).encode('utf-8')).hexdigest()
