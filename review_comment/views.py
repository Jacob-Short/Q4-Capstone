# from django.contrib.auth.models import User
from django.shortcuts import redirect, render, HttpResponseRedirect
from review.models import Review
from review_comment.models import ReviewComment
from django.views.generic import View
from review_comment.forms import AddReviewCommentForm
from message.models import Message
from review_comment.models import ReviewComment
from review_notification.views import create_review_notification

# from review.models import User

from all_notifications.views import get_notification_count


class CreateReviewComment(View):
    def get(self, request, id):
        target_user = request.user.id
        messages = Message.objects.filter(recipient=target_user)

        notifications_count = get_notification_count(request.user)

        form = AddReviewCommentForm()
        context = {
            "form": form,
            "messages": messages,
            "notifications_count": notifications_count,
        }
        return render(request, "generic_form.html", context)

    def post(self, request, id):
        review = Review.objects.get(id=id)
        form = AddReviewCommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_comment = ReviewComment.objects.create(
                comment=data["comment"],
                review=review,
                user_created=request.user,
            )
            created_review = review.user_created
            create_review_notification(review, created_review)
            return redirect("homepage")


class ReplyToReviewComment(View):
    '''reply to a users comment on a faq'''
    def get(self, request, id):
        form = AddReviewCommentForm()
        template = 'generic_form.html'
        target_user = request.user.id
        messages = Message.objects.filter(recipient=target_user)

        notifications_count = get_notification_count(request.user)
        context = {
            "messages": messages,
            "form": form,
            "notifications_count": notifications_count,
        }
        return render(request, template, context)

    def post(self, request, id):
        comment = ReviewComment.objects.get(id=id)
        comment_review = comment.review.id
        review = Review.objects.get(id=comment_review)
        review_created = review.user_created
        form = AddReviewCommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_comment = ReviewComment.objects.create(
                comment=data["comment"],
                user_created=request.user,
                review=review,
                parent=comment
            )
            create_review_notification(review, review_created)
            return redirect("homepage")



