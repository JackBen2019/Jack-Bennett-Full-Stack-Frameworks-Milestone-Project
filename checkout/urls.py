from django.conf.urls import url
from .views import checkout, delete_order

urlpatterns = [
    url(r'^$', checkout, name="checkout"),
    url(r'^delete_order/(?P<pk>\d+)/$', delete_order, name="delete_order")
]