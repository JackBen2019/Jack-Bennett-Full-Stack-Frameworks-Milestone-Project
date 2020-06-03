from django.conf.urls import url
from .views import do_search_product, do_search_forum

urlpatterns = [
    url(r'^$', do_search_product, name='search_product'),
    url(r'^$', do_search_forum, name='search_forum')
]