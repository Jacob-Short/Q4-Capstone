from django.urls import path
from all_notifications import views as notification_views


urlpatterns = [
    path('notifications/', notification_views.notification_view, name='notis'),
]