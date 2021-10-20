from django.shortcuts import render, redirect
from django.views.generic import View
from community.models import Community
from games.models import Game
from review.models import Review
from review.forms import CreateReviewForm

from community import settings
from message.models import Message
from review_comment.models import ReviewComment

from all_notifications.views import get_notification_count



class CreateReview(View):
    '''can create a review on a game in db'''

    def get(self, request, id):
        template = 'generic_form.html'
        form = CreateReviewForm()
        target_user = request.user.id
        messages = Message.objects.filter(recipient=target_user)
        context = {'messages': messages, 'form': form}
        return render(request, template, context)


    def post(self, request, id):
        form = CreateReviewForm(request.POST)
        game = Game.objects.get(id=id)
        if form.is_valid():
            data = form.cleaned_data
            review = Review.objects.create(
                rating = data['rating'],
                name = data['name'],
                text = data['text'],
                game = game,
                user_created = request.user,
            )
            if game not in settings.review_users:
                settings.review_users[game] = [request.user]
            else:
                settings.review_users[game].append(request.user)
            return redirect('/')


class Reviews(View):
    """displays all reviews"""
    def get(self, request):
      reviews = Review.objects.all()
      template = "reviews.html"
      context = {'reviews':reviews}
      return render(request, template, context)


    def post(self, request):
      ...

class ReviewDetailView(View):
    
    def get(self, request, id):
        review = Review.objects.get(id=id)
        comments = ReviewComment.objects.filter(review=review)


        notifications_count = get_notification_count(request.user)

        messages = Message.objects.filter(recipient=request.user)

        template = 'review_detail.html'
        comments = ReviewComment.objects.filter(review=review)
        context = {'review': review, 'comments': comments, 'notifications_count': notifications_count, 'messages': messages}

        return render(request, template, context)

    def post(self, request):
        ...

class FilteredReviews(View):

    def get(self, request, game_name):
        reviews = Review.objects.filter(game=game_name)
        template = 'review_detail.html'
        context = {'reviews': reviews}

        return render (request, template, context)

    def post(self, request):
        ...


def delete_review(request, id):
    review = Review.objects.get(id=id)
    review.delete()
    return redirect('/')
