from django.urls import path
from accounts import views as account_views

urlpatterns = [
    path('', account_views.IndexView.as_view(), name='homepage'),
]