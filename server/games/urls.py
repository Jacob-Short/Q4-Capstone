from django.conf.urls import include, url

from games.views import GamesViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register('games', GamesViewSet)

#  using regex so it will ONLY work at localhost 5000
urlpatterns = [
    url(r"^games/", include(router.urls))
]