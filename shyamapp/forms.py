from django import forms
from .models import CustomerReview

class CustomerReviewForm(forms.ModelForm):
    class Meta:
        model = CustomerReview
        fields = ['name', 'review', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'review': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Your Review'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }
