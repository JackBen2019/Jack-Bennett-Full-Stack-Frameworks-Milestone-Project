from django import forms


class ContactForm(forms.Form):

    email_address = forms.EmailField(required=True)
    reason = forms.CharField(required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
