from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from .forms import PaymentDataForm
from .logic import get_security_key
from .settings import CONFIG
from .signals import result_received


class PayView(View):

    def get_order_id(self):
        return unicode(self.request.session.get('payonline_order_id'))

    def get_amount(self):
        return u'%.2f' % self.request.session.get('payonline_amount')

    def get_merchant_id(self):
        return CONFIG['MERCHANT_ID']

    def get_currency(self):
        return CONFIG['CURRENCY']

    def get_private_security_key(self):
        return CONFIG['PRIVATE_SECURITY_KEY']

    def _get_security_key(self):
        return get_security_key(
            self.get_order_id(),
            self.get_amount(),
            merchant_id=self.get_merchant_id(),
            currency=self.get_currency(),
            private_security_key=self.get_private_security_key())

    def get_context_data(self, **kwargs):
        kwargs.update({'order_id': self.get_order_id(),
                       'amount': self.get_amount(),
                       'merchant_id': self.get_merchant_id(),
                       'currency': self.get_currency(),
                       'security_key': self._get_security_key()})
        return kwargs

    def get(self, request, *args, **kwargs):
        return render(request, 'payonline/pay.html', self.get_context_data())


class CallbackView(View):

    def get_private_security_key(self):
        return CONFIG['PRIVATE_SECURITY_KEY']

    def get_form(self, data):
        return PaymentDataForm(data=data, private_security_key=self.get_private_security_key())

    def process_form(self, form):
        if form.is_valid():
            payment = form.save()
            result_received.send(
                sender=payment,
                OrderId=form['OrderId'],
                Amount=form['Amount'],
            )
            return HttpResponse()
        return HttpResponseBadRequest()

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CallbackView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.process_form(self.get_form(request.GET or None))

    def post(self, request, *args, **kwargs):
        return self.process_form(self.get_form(request.POST or None))


class FailView(View):

    def post(self, request, *args, **kwargs):
        if 'ErrorCode' not in request.POST:
            return HttpResponseBadRequest()
        return render(request, 'payonline/fail.html', {
            'error_code': request.POST['ErrorCode'],
        })


class SuccessView(View):

    def get_context_data(self, **kwargs):
        return kwargs

    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data()
        return render(request, 'payonline/success.html', context_data)
