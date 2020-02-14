from django import forms
from .models import contact_tble

class contact_tbleForm(forms.ModelForm):
    model = contact_tble
    fields ='__all__'