from django import forms
from localflavor.in_.forms import INStateSelect, INZipCodeField
from .models import Order

class OrderCreateForm(forms.ModelForm):
  first_name  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name...'}))
  last_name   = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name...'}))
  email       = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email...'}))
  address     = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address...'}))
  postal_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Postal Code...'}))
  city        = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City...'}))
  postal_code = INZipCodeField()

  class Meta:
    model = Order
    fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
    