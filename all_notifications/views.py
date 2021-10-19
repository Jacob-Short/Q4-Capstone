from django.shortcuts import render, HttpResponseRedirect, reverse
from message.models import Message
from message_notification.models import MessageNotification
from review_notification.models import ReviewNotification
from faq_notification.models import FaqNotification

# from message_notification.models import MessageNotification
from accounts.models import MyUser


def notification_view(request):
    target_user = request.user
    new_notifications = []

    message_notifications = MessageNotification.objects.filter(
        user_notified=target_user
    )
    review_notifications = ReviewNotification.objects.filter(user_notified=target_user)
    faq_notifications = FaqNotification.objects.filter(user_notified=target_user)

    all_notifications = list(message_notifications) + list(review_notifications) + list(faq_notifications)

    notifications_count = len(all_notifications)

    print(all_notifications)
    print(f'messages: {message_notifications}')
    print(f'reviews: {review_notifications}')

    context = {
        "request": request,
        "notifications_count": notifications_count,
        "message_notifications": message_notifications,
        "review_notifications": review_notifications,
        "faq_notifications": faq_notifications,
    }
    return render(request, "notifications.html", context)
