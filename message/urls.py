from django.urls import path
from . import views

urlpatterns = [
    path('/message', account_views.MessageView, name='messages'),
   
]