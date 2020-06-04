from django.conf.urls import url, include
from django.http import HttpResponse
from .views import index, get_forum, forum_post_details, create_forum_post, edit_forum_post, general_discussion
from accounts.views import logout, login, registration, user_profile, about, customer, dashboard, customer_no_orders
from products.views import all_products, product_details, edit_product, add_product
from accounts import url_reset

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^about/', about, name="about"),
    url(r'^dashboard/', dashboard, name="dashboard"),
    url(r'^user-profile/', customer_no_orders, name="customer_no_orders"),
    url(r'^(?P<pk>\d+)/user-profile/$', customer, name="customer"),
    url(r'^forum/', get_forum, name='get_forum'),
    url(r'^general-discussion/', general_discussion, name='general_discussion'),
    url(r'^password-reset/', include(url_reset)),
    url(r'^(?P<pk>\d+)/$', forum_post_details, name='forum_post_details'),
    url(r'^new/$', create_forum_post, name='create_forum_post'),
    url(r'^(?P<pk>\d+)/edit/$', edit_forum_post, name='edit_forum_post')
]