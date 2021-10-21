from django.shortcuts import render, HttpResponseRedirect, reverse
from message.models import Message
from message_notification.models import MessageNotification
from review_notification.models import ReviewNotification
from faq_notification.models import FaqNotification

# from message_notification.models import MessageNotification
from accounts.models import MyUser
from django.db.models import Q

def notify_seen(notifications):
    for noti in notifications:
        noti.isNew = False
        noti.save()

def get_notification_count(logged_in_user):
    target_user = logged_in_user
    new_notifications = []

    new_message_notifications = MessageNotification.objects.filter(
        Q(user_notified=target_user) & Q(isNew=True)
    )
    new_review_notifications = ReviewNotification.objects.filter(
        Q(user_notified=target_user) & Q(isNew=True)
    )
    new_faq_notifications = FaqNotification.objects.filter(
        Q(user_notified=target_user) & Q(isNew=True)
    )

    new_notifications = (
        list(new_message_notifications)
        + list(new_review_notifications)
        + list(new_faq_notifications)
    )

    notifications_count = len(new_notifications)
    return notifications_count



def notification_view(request):
    target_user = request.user
    new_notifications = []
    user_messages = Message.objects.filter(recipient=target_user)
    new_message_notifications = MessageNotification.objects.filter(
        Q(user_notified=target_user) & Q(isNew=True)
    )
    new_review_notifications = ReviewNotification.objects.filter(
        Q(user_notified=target_user) & Q(isNew=True)
    )
    new_faq_notifications = FaqNotification.objects.filter(
        Q(user_notified=target_user) & Q(isNew=True)
    )

    new_notifications = (
        list(new_message_notifications)
        + list(new_review_notifications)
        + list(new_faq_notifications)
    )

    notifications_count = get_notification_count(request.user)

    # old notifications
    old_message_notifications = MessageNotification.objects.filter(
        Q(user_notified=target_user) & Q(isNew=False)
    )
    old_review_notifications = ReviewNotification.objects.filter(
        Q(user_notified=target_user) & Q(isNew=False)
    )
    old_faq_notifications = FaqNotification.objects.filter(
        Q(user_notified=target_user) & Q(isNew=False)
    )

    old_notifications = (
        list(old_message_notifications)
        + list(old_review_notifications)
        + list(old_faq_notifications)
    )

    print(new_notifications)
    print(f"user_messages: {new_message_notifications}")
    print(f"reviews: {new_review_notifications}")

    context = {
        "request": request,
        "notifications_count": notifications_count,
        "new_message_notifications": new_message_notifications,
        "new_review_notifications": new_review_notifications,
        "new_faq_notifications": new_faq_notifications,
        "old_notifications": old_notifications,
        "user_messages": user_messages
    }

    notify_seen(new_notifications)
    return render(request, "notifications.html", context)


