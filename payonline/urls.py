from django.conf.urls import re_path
from .views import PayView, CallbackView, FailView, SuccessView


urlpatterns = [
    re_path(r'^$', PayView.as_view(), name='payonline_pay'),
    re_path(r'^callback/$', CallbackView.as_view(), name='payonline_callback'),
    re_path(r'^fail/$', FailView.as_view(), name='payonline_fail'),
    re_path(r'^success/$', SuccessView.as_view(), name='payonline_success'),
]
