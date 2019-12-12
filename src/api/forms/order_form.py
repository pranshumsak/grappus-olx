from django import forms

from api.models.order_models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'
