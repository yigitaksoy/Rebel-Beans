from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


    def __init__(self, *args, **kwargs):
        """ Add Placeholder texts and classes for the form """

        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Your name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Let us know how we can help!',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'