from django.urls import path
from games import views as game_views


urlpatterns = [
    path('games/', game_views.GamesHomeView.as_view(), name='games'),
]