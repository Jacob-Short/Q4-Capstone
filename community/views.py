from django.shortcuts import redirect, render, reverse, HttpResponseRedirect
from django.views.generic import View

from .models import Community
from games.models import Game

from .forms import CreateCommunityForm

class AbilityToCreateCommunity(View):
    '''when 2 or more users leave a review and faq on the same
    game, a community will then become available to create'''
    
    def get(self, request, id):
        template = 'generic_form.html'
        form = CreateCommunityForm()
        context = {'form': form}
        return render(request, template, context)


    def post(self, request, id):
        form = CreateCommunityForm(request.POST)
        game = Game.objects.get(id=id)
        if form.is_valid():
            data = form.cleaned_data
            community = Community.objects.create(
                creator=request.user,
                game=game,
                members=data['members'],
            )
            return HttpResponseRedirect(reverse("homepage"))