from django.shortcuts import render, HttpResponseRedirect, reverse
from review.models import Review
from review_notification.models import ReviewNotification
from accounts.models import MyUser


def notification_view(request):
    target_user = request.user
    new_notifications = []
    notifications = ReviewNotification.objects.all().order_by('-id')

    if len(notifications) > 1:
        no_new_notifs = 'You have no new notifications!'

    context = {'request': request, 'notifications': notifications, 'no_new_notifs': no_new_notifs}
    return render(request, 'notifications.html', context)

def create_notification(review, tagged):
    all_users = MyUser.objects.all()
    names = [x.username for x in all_users]
    print(names)
    user_string = ''
    for person in tagged:
        user_string += person
    print(user_string)
    target_user = MyUser.objects.get(username=user_string)
    notification = ReviewNotification.objects.create(
        message = review,
        user_notified = target_user,
    )

def notify_seen(request):
    notification = ReviewNotification.objects.all()[::-1]
    seen_notification = notification[0]
    seen_notification.isNew = False
    seen_notification.save()
    return HttpResponseRedirect(reverse('home'))