from django.conf.urls import url
from django.urls import path
from django.views.generic.base import RedirectView

from tweets.api.views import TweetListAPIView
from . import views
urlpatterns = [
    path('', TweetListAPIView.as_view(), name='list')
    # url(r'^$', RedirectView.as_view(url="/")),
    # url(r'^search/$', TweetListView.as_view(), name='list'), # /tweet/
    # url(r'^create/$', TweetCreateView.as_view(), name='create'), # /tweet/create/
    # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1/
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), # /tweet/1/update/
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), # /tweet/1/delete/
]