from django.conf.urls import url, include
from django.http import HttpResponse
from .views import get_forum, forum_details, create_or_edit_forum
from accounts.views import logout, login, registration, user_profile, about, customer, dashboard
from products.views import all_products, product_details, edit_product, add_product
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^about/', about, name="about"),
    url(r'^customer/', customer, name="customer"),
    url(r'^dashboard/', dashboard, name="dashboard"),
    url(r'^forum/', get_forum, name='get_forum'),
    url(r'^password-reset/', include(url_reset)),
    url(r'^(?P<pk>\d+)/$', forum_details, name='forum_details'),
    url(r'^new/$', create_or_edit_forum, name='add_forum'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_forum, name='edit_forum')
]