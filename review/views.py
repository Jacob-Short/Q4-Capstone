from django.shortcuts import render, redirect
from django.views.generic import View
from games.models import Game
from review.models import Review
from review.forms import CreateReviewForm

from review_comment.models import ReviewComment 


class CreateReview(View):
    '''can create a review on a game in db'''

    def get(self, request, id):
        template = 'generic_form.html'
        form = CreateReviewForm()
        context = {'form': form}
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

        template = 'review_detail.html'
        comments = ReviewComment.objects.filter(review=review)
        context = {'review': review, 'comments': comments}

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
