from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['reason']
            from_email = form.cleaned_data['email_address']
            message = form.cleaned_data['description']
            try:
                send_mail(subject, message, from_email,
                          ['jackbennett@jbmarketing.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact_success')
    return render(request, 'contact_email.html', {'form': form})


def contact_success(request):
    return render(request, 'contact_success.html')
