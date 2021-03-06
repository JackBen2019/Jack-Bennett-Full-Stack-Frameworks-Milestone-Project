from django.conf.urls import url
from .views import all_products, product_details, edit_product, add_product

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<pk>\d+)/$', product_details, name='product_details'),
    url(r'^new/$', add_product, name='add_product'),
    url(r'^edit/(?P<pk>\d+)/$', edit_product, name='edit_product')
]