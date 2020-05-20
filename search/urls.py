from django.conf.urls import url
from .views import do_search_product, do_search_review

urlpatterns = [
    url(r'^$', do_search_product, name='search_product'),
    url(r'^$', do_search_review, name='search_review')
]