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
            subject = form.cleaned_data['contact_subject']
            from_email = form.cleaned_data['contact_from_email']
            message = form.cleaned_data['contact_message']
            try:
                send_mail(subject, message, from_email,
                          ['jackbennett@jbmarketing.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact_success')
    return render(request, "email.html", {'form': form})


def contact_success(request):
    return HttpResponse('Thanks for your message.')
