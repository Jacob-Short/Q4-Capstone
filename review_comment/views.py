# from django.contrib.auth.models import User
from django.shortcuts import redirect, render, HttpResponseRedirect
from review.models import Review
from review_comment.models import ReviewComment
from django.views.generic import View
from review_comment.forms import AddReviewCommentForm

from review_comment.models import ReviewComment
from review_notification.views import create_review_notification
# from review.models import User

class CreateReviewComment(View):

    def get(self, request, id):
        form = AddReviewCommentForm()
        context = {'form': form}
        return render(request, 'generic_form.html', context)

    def post(self, request, id):
        review = Review.objects.get(id=id)
        form = AddReviewCommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_comment = ReviewComment.objects.create(
                comment = data['comment'],
                parent = data['parent'],
                review = review,
                user_created = request.user,
            )
            created_review = review.user_created
            create_review_notification(review, created_review)
            return redirect('homepage')