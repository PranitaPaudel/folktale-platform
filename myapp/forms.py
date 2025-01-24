from django import forms
from .models import Newsletter

class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email', 
                'required': 'required'
            })
        }