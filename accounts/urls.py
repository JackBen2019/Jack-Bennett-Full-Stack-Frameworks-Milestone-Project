from django.conf.urls import url, include
from .views import get_reviews, review_details, create_or_edit_review
from accounts.views import logout, login, registration, user_profile
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^reviews/', get_reviews, name='get_reviews'),
    url(r'^password-reset/', include(url_reset)),
    url(r'^(?P<pk>\d+)/$', review_details, name='review_details'),
    url(r'^new/$', create_or_edit_review, name='add_review'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_review, name='edit_review')
]