from django.contrib import admin
from django.conf.urls import url
from.views import contact, contact_success
from .models import ContacForm

urlpatterns = [
    url(r'^contact-us/', contact, name="contact"),
    url(r'^success/', contact_success, name="contact_success"),
]