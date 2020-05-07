from django.conf.urls import url, include
from.views import all_products


url_patterns = [
    url(r'^$', all_products, name='products'),
    ]