from django.urls import path
from games import views as game_views


urlpatterns = [
    path('games_home/', game_views.FillDbWithGames.as_view(), name='api_homepage'),
]