from django.urls import path
from message import views

urlpatterns = [
    path('message/user/<int:id>', views.MessageView, name='messages'),   
]