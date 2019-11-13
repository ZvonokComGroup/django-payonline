

class DataProxy(object):

    aliases = {
        'datetime': 'DateTime',
        'transaction_id': 'TransactionID',
        'order_id': 'OrderId',
        'amount': 'Amount',
        'currency': 'Currency',
        'payment_amount': 'PaymentAmount',
        'payment_currency': 'PaymentCurrency',
        'card_holder': 'CardHolder',
        'card_number': 'CardNumber',
        'country': 'Country',
        'city': 'City',
        'address': 'Address',
        'ip_address': 'IpAddress',
        'ip_country': 'IpCountry',
        'bin_country': 'BinCountry',
        'special_conditions': 'SpecialConditions',
        'provider': 'Provider',
        'rebill_anchor': 'RebillAnchor',
    }

    def __init__(self, data):
        self.data = data

    def __getitem__(self, name):
        if name in self.aliases:
            name = self.aliases[name]
        return self.data[name]

    def get(self, name, default=None):
        if name in self.aliases:
            name = self.aliases[name]
        return self.data.get(name, default)
