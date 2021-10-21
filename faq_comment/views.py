from django.contrib.auth.models import User
from django.shortcuts import redirect, render, HttpResponseRedirect
from faq_comment.models import FaqComment
from django.views.generic import View
from faq_comment.forms import AddFaqCommentForm

from faq_comment.models import FaqComment
from faq.models import UserFaq
from message.models import Message
from faq_notification.models import FaqNotification
from faq_notification.views import create_faq_notification
from django.contrib import messages

from all_notifications.views import get_notification_count


class CreateFaqComment(View):
    """can create a comment on a review"""

    def get(self, request, id):
        form = AddFaqCommentForm()
        target_user = request.user.id
        user_messages = Message.objects.filter(recipient=target_user)

        notifications_count = get_notification_count(request.user)
        context = {
            "user_messages": user_messages,
            "form": form,
            "notifications_count": notifications_count,
        }
        return render(request, "generic_form.html", context)

    def post(self, request, id):
        faq = UserFaq.objects.get(id=id)
        faq_created = faq.user
        form = AddFaqCommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_comment = FaqComment.objects.create(
                comment=data["answer"],
                user=request.user,
                faq=faq,
            )
            messages.add_message(
                request, message="Question answered.", level=messages.SUCCESS
            )
            create_faq_notification(faq, faq_created)
            return redirect("homepage")


class ReplyToFaqComment(View):
    '''reply to a users comment on a faq'''
    def get(self, request, id):
        form = AddFaqCommentForm()
        template = 'generic_form.html'
        target_user = request.user.id
        user_messages = Message.objects.filter(recipient=target_user)

        notifications_count = get_notification_count(request.user)
        context = {
            "user_messages": user_messages,
            "form": form,
            "notifications_count": notifications_count,
        }
        return render(request, template, context)

    def post(self, request, id):
        comment = FaqComment.objects.get(id=id)
        comment_faq = comment.faq.id
        faq = UserFaq.objects.get(id=comment_faq)
        faq_created = faq.user
        form = AddFaqCommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_comment = FaqComment.objects.create(
                comment=data["answer"],
                user=request.user,
                faq=faq,
                parent=comment
            )
            messages.add_message(
                request, message="Reply sent.", level=messages.SUCCESS
            )
            create_faq_notification(faq, faq_created)
            return redirect("homepage")