"""tweetme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from accounts.views import UserDetailView, UserFollowView
from tweets.api.views import TweetListAPIView, TweetCreateAPIView
from .views import home
# from tweets.views import tweet_detail_view, tweet_list_view
from tweets.views import TweetListView, TweetDetailView, tweet_detail_view, TweetCreateView, TweetUpdateView, \
    TweetDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name='home'),

    # tweets



    # path('', RedirectView.as_view(url="/")),
    path('api/tweet/', TweetListAPIView.as_view(), name='list'),
    path('api/tweet/create/', TweetCreateAPIView.as_view(), name='create'),
    # path('api/tweet/', include('tweets.api.urls', namespace='tweet-api')),
    path('', TweetListView.as_view(), name='home'),
    path('tweet/<int:pk>/', tweet_detail_view, name='detail'),
    path('tweet/<int:pk>/update/', TweetUpdateView.as_view(), name='update'),
    path('tweet/<int:pk>/delete/', TweetDeleteView.as_view(), name='delete'),
    path('tweet/create/', TweetCreateView.as_view(), name='create'),

    path('profile/<slug:username>', UserDetailView.as_view(), name='profile-detail'),
path('profile/<slug:username>/follow/', UserFollowView.as_view(), name='follow')
]
# if settings.DEBUG:
#     urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
