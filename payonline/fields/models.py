from django.db import models
from . import forms


class UTCDateTimeField(models.DateTimeField):

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.UTCDateTimeField}
        defaults.update(kwargs)
        return super(UTCDateTimeField, self).formfield(**kwargs)
