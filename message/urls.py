from django.urls import path
from message import views

urlpatterns = [
    path('message/user/<int:id>', views.MessageView, name='message'), 
    path('user/<int:id>/messages', views.UserMessages, name='usermessages')  
]