from django.shortcuts import render, redirect
from django.views.generic import View

from games.models import Game
from review.models import Review
from review.forms import CreateReviewForm


class CreateReview(View):
    '''can create a review on a game in db'''

    def get(self, request):
        template = 'create_review.html'
        form = CreateReviewForm()
        context = {'form': form}
        return render(request, template, context)


    def post(self, request):
        form = CreateReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            review = Review.objects.create(
                name = data['name'],
                text = data['text'],
                game = data['game'],
                user_created = request.user,
            )
            return redirect('/')
