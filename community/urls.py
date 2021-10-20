from django.urls import path
from community import views as community_views


urlpatterns = [
    path('create_community/', community_views.CreateCommunity.as_view(), name='create_new_communitys'),
    path('community/<int:id>/', community_views.CommunityView.as_view(), name='community'),
]