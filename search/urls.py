from django.conf.urls import url
from .views import do_search_product

urlpatterns = [
    url(r'^$', do_search_product, name='search_product')
]