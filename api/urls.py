from django.urls import path
from api import views as api_views


urlpatterns = [
    path('api_home/', api_views.ApiHomeView.as_view(), name='api_homepage'),
    path('api_all_games/', api_views.ApiAllGamesView.as_view(), name='api_all_games'),
]