from django.conf.urls import url
from .views import checkout, deleteOrder
from accounts import urls as accounts_urls

urlpatterns = [
    url(r'^$', checkout, name="checkout"),
    url(r'^(?P<pk>\d+)/delete_order/$', deleteOrder, name="delete_order")
]