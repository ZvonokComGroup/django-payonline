from django.dispatch import Signal

result_received = Signal(providing_args=["OrderId", "Amount"])
