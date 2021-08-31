from django import forms

from .models import County


class CheckoutForm(forms.Form):
    __counties = County.objects.all()
    fname = forms.CharField(max_length=50, label='Nume')
    lname = forms.CharField(max_length=50, label='Prenume')
    email = forms.EmailField(label='Email')
    customer_type = forms.ChoiceField(choices=[('P', 'Persoană'), ('C', 'Companie')], initial='P', widget=forms.RadioSelect)
    phone = forms.CharField(max_length=10, min_length=10, label='Numar de telefon')
    street = forms.CharField(widget=forms.Textarea, label='Strada')
    county = forms.ModelChoiceField(queryset=__counties, label='Județ', empty_label='Alege o regiune')
    city = forms.ChoiceField(label='Oraș', disabled=True)

    fname.widget.attrs.update({
        'class': 'form-control',
    })

    lname.widget.attrs.update({
        'class': 'form-control',
    })

    email.widget.attrs.update({
        'class': 'form-control',
    })

    phone.widget.attrs.update({
        'class': 'form-control',
    })

    county.widget.attrs.update({
        'class': 'form-control',
    })

    city.widget.attrs.update({
        'class': 'form-control',
    })

    street.widget.attrs.update({
        'class': 'form-control',
        'rows': 3,
    })
