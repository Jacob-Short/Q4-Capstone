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

def create_notification(message, tagged):
    all_users = MyUser.objects.all()
    names = [x.username for x in all_users]
    print(names)
    user_string = ''
    for person in tagged:
        user_string += person
    print(user_string)
    target_user = MyUser.objects.get(username=user_string)
    notification = MessageNotification.objects.create(
        message = message,
        user_notified = target_user,
    )

def notify_seen(request):
    notification = MessageNotification.objects.all()[::-1]
    seen_notification = notification[0]
    seen_notification.isNew = False
    seen_notification.save()
    return HttpResponseRedirect(reverse('home'))