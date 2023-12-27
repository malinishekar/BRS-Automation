from django import forms
from django.forms import ModelForm
from .models import Venu

class VenueForm(ModelForm):
    class Meta:
        model = Venu
        fields = ('name', 'address', 'phone', 'web', 'email_address')
