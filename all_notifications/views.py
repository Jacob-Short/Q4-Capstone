from django.shortcuts import render, HttpResponseRedirect, reverse
from message.models import Message
from message_notification.models import MessageNotification
from accounts.models import MyUser


def notification_view(request):
    target_user = request.user
    new_notifications = []
    notifications = MessageNotification.objects.all().order_by('-id')

    if len(notifications) > 1:
        no_new_notifs = 'You have no new notifications!'

    context = {'request': request, 'notifications': notifications, 'no_new_notifs': no_new_notifs}
    return render(request, 'notifications.html', context)

