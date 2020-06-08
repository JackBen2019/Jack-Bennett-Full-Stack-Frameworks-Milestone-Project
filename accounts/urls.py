from django.conf.urls import url, include
from .views import (
    index,
    get_forum,
    forum_post_details,
    create_forum_post,
    edit_forum_post,
    gen_discussion,
    events,
    privacy_policy)
from .views import (
    logout,
    login,
    registration,
    about,
    profile,
    dashboard,
    profile_no_orders,
    edit_profile)
from accounts import url_reset

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^privacy-policy/', privacy_policy, name="privacy_policy"),
    url(r'^about/', about, name="about"),
    url(r'^dashboard/', dashboard, name="dashboard"),
    url(r'^(?P<pk>\d+)/user-profile/$', profile, name="profile"),
    url(r'^user-profile/', profile_no_orders, name="profile_no_orders"),
    url(r'^edit-profile/$', edit_profile, name="edit_profile"),
    url(r'^forum/', get_forum, name='get_forum'),
    url(r'^general-discussion/', gen_discussion, name='gen_discussion'),
    url(r'^events/', events, name='events'),
    url(r'^password-reset/', include(url_reset, namespace=None)),
    url(r'^(?P<pk>\d+)/$', forum_post_details, name='forum_post_details'),
    url(r'^new/$', create_forum_post, name='create_forum_post'),
    url(r'^(?P<pk>\d+)/edit/$', edit_forum_post, name='edit_forum_post')
]
