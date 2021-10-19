"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from accounts.urls import urlpatterns as account_url
from message.urls import urlpatterns as message_url
from api.urls import urlpatterns as api_url
from games.urls import urlpatterns as game_url
from review.urls import urlpatterns as review_url
from faq.urls import urlpatterns as faq_url
from faq_comment.urls import urlpatterns as faq_comment_url
from community.urls import urlpatterns as community_comment_url

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += account_url
urlpatterns += api_url
urlpatterns += message_url
urlpatterns += game_url
urlpatterns += review_url
urlpatterns += faq_url
urlpatterns += faq_comment_url
urlpatterns += community_comment_url