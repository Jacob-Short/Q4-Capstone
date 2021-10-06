from django.urls import path
from message import views

urlpatterns = [
    path('message/', views.MessageView, name='messages'),   
]