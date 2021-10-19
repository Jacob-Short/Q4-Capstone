from django.shortcuts import render, HttpResponseRedirect, reverse
from review.models import Review
from review_notification.models import ReviewNotification
from accounts.models import MyUser


def create_review_notification(review, tagged):
    all_users = MyUser.objects.all()
    names = [x.username for x in all_users]
    print(names)
    user_string = ''
    user_string += str(tagged)
    print(user_string)
    target_user = MyUser.objects.get(username=user_string)
    notification = ReviewNotification.objects.create(
        review = review,
        user_notified = target_user,
    )

def notify_seen(request):
    notification = ReviewNotification.objects.all()[::-1]
    seen_notification = notification[0]
    seen_notification.isNew = False
    seen_notification.save()
    return HttpResponseRedirect(reverse('home'))