from django.urls import path
from api import views as api_views

urlpatterns = [
    path('api_home/', api_views.ApiHomeView.as_view(), name='api_homepage'),
]