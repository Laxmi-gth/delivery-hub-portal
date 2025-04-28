from django import forms
from .models import CustomerEnquiry


class CustomerEnquiryForm(forms.ModelForm):
    class Meta:
        model=CustomerEnquiry
        fields=['customer_name','phone','email','query']