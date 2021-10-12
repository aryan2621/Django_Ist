from django import forms
from .models import Shopping


class ShoppingForm(forms.ModelForm):
    class Meta:
        model = Shopping
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(required=True)
    description = forms.CharField()
    price = forms.DecimalField()
