from django.forms import ModelForm
from models import Order


class CheckoutForm(ModelForm):
    class Meta:
        model = Order
        fields = []
        # exclude = []
