from django.urls import path
from games import views as game_views


urlpatterns = [
    path('games/', game_views.GamesHomeView.as_view(), name='games'),
    path('create_game/', game_views.CreateGameView.as_view(), name='create_game'),
    path('game_detail/<int:id>', game_views.GameDetailView.as_view(), name='game_detail'),
    path('filter_games/', game_views.filtered_games, name='filtered_games'),
]