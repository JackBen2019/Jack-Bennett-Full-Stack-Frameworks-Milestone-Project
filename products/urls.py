from django.conf.urls import url, include
from .views import all_products, product_details, create_or_edit_product

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<pk>\d+)/$', product_details, name='product_details'),
    url(r'^new/$', create_or_edit_product, name='add_product'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_product, name='edit_product')
]