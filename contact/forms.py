from django import forms
from .models import contactDetails

class ContactForm(forms.ModelForm):

    class Meta:
        model = contactDetails
        fields = '__all__'
