from django import forms


class ContactForm(forms.Form):
    contact_from_email = forms.EmailField(required=True)
    contact_subject = forms.CharField(required=True)
    contact_message = forms.CharField(widget=forms.Textarea, required=True)
