from django import forms
from .models import country

class countryForm(forms.ModelForm):
    class Meta:

        model = country
        fields = ['country_name','currency','country_image']