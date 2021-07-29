from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class ReviewForm(forms.Form):
    stars = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], widget=forms.HiddenInput())
    text_review = forms.CharField(widget=forms.Textarea)

    stars.widget.attrs.update({
        'id': 'rating-hidden',
        'min': 1,
        'max': 5,
        'class': 'hidden',
    })

    text_review.widget.attrs.update({
        'id': 'review',
        'class': 'md-textarea form-control pr-6 md-form md-outline row align-items-center review-input',
        'rows': 4,
    })

    error_css_class = 'error'
    required_css_class = 'warning'
