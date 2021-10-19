from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Message
from accounts.models import MyUser
from .forms import AddTextForm

from message_notification.views import create_message_notification


from message_notification.models import MessageNotification
from review_notification.models import ReviewNotification
from faq_notification.models import FaqNotification


def MessageView(req, id):
    template = "generic_form.html"
    if req.method == "POST":
        recip = MyUser.objects.get(id=id)
        form = AddTextForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            message = Message.objects.create(
                message=data["message"], author=req.user, recipient=recip
            )
            create_message_notification(message, recip)

            return HttpResponseRedirect(reverse("profile", args=(id,)))
    form = AddTextForm()
    return render(req, "generic_form.html", {"form": form, "header": "message"})


def UserMessages(req, id):
    target_user = MyUser.objects.get(id=id)

    message_notifications = MessageNotification.objects.filter(
        user_notified=target_user
    )
    review_notifications = ReviewNotification.objects.filter(user_notified=target_user)
    faq_notifications = MessageNotification.objects.filter(user_notified=target_user)
    all_notifications = (
        list(message_notifications)
        + list(review_notifications)
        + list(faq_notifications)
    )
    notifications_count = len(all_notifications)

    messages = Message.objects.filter(recipient=target_user)
    context = {
        "messages": messages,
        "notifications_count": notifications_count
    }
    return render(req, "messages.html", context)


def DeleteMessage(req, id):
    del_message = Message.objects.get(id=id)
    user_id = req.user.id
    del_message.delete()
    return HttpResponseRedirect(reverse("usermessages", args=(user_id,)))
