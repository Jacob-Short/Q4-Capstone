from django.contrib.auth.models import User
from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Message
from accounts.models import MyUser
from .forms import AddTextForm

from message_notification.views import create_message_notification


from message_notification.models import MessageNotification
from review_notification.models import ReviewNotification
from faq_notification.models import FaqNotification

from all_notifications.views import get_notification_count

from django.contrib import messages


def get_messages_count(logged_in_user):
    target_user = logged_in_user
    user_messages = Message.objects.filter(recipient=target_user)

    messages_count = len(user_messages)
    return messages_count


def MessageView(req, id):
    template = "generic_form.html"
    recip = MyUser.objects.get(id=id)
    signed_in_user = req.user
    user_messages = Message.objects.filter(recipient=recip)
    if req.method == "POST":
        form = AddTextForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            message = Message.objects.create(
                message=data["message"], author=req.user, recipient=recip
            )
            create_message_notification(message, recip)
            messages.add_message(req, message="Message sent.", level=messages.SUCCESS)
            return HttpResponseRedirect(reverse("profile", args=(id,)))
    form = AddTextForm()
    context = {
        "user_messages": user_messages,
        "form": form,
        "header": "message",
        "signed_in_user": signed_in_user,
    }
    return render(req, "generic_form.html")


def UserMessages(req, id):
    target_user = MyUser.objects.get(id=id)
    signed_in_user = MyUser.objects.get(id=req.user.id)

    notifications_count = get_notification_count(req.user)

    user_messages = Message.objects.filter(recipient=target_user)
    context = {
        "user_messages": user_messages,
        "notifications_count": notifications_count,
        "signed_in_user": signed_in_user,
        "target_user": target_user
    }
    return render(req, "messages.html", context)


def DeleteMessage(req, id):
    del_message = Message.objects.get(id=id)
    user_id = req.user.id
    del_message.delete()
    messages.add_message(req, message="Message deleted.", level=messages.ERROR)
    return HttpResponseRedirect(reverse("usermessages", args=(user_id,)))
