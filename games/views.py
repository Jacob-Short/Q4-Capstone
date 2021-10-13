from django.shortcuts import render, redirect
from django.views.generic import View
from api.models import ApiSearch
from games.models import Game
from games.forms import CreateGameForm, SearchGameForm

import ast



class GamesHomeView(View):
    '''view alll games in db'''

    def get(self, request):
        games = Game.objects.all()
        template = 'games.html'

        form = SearchGameForm()

        switch_games = []
        xbox_games = []
        playstation_games = []
        pc_games = []

        for game in games:
            spec_game = game.plaftorm
            if spec_game == "Xbox One" or spec_game == "Xbox 360":
                xbox_games.append(game)
            elif (
                spec_game == "PlayStation 4"
                or spec_game == "PlayStation 4"
                or spec_game == "PlayStation 3"
            ):
                playstation_games.append(game)
            elif spec_game == "PC":
                pc_games.append(game)
            elif spec_game == "Nintendo Switch":
                switch_games.append(game)



        context = {
            "games": games,
            "form": form,
            "pc_games": pc_games,
            "playstation_games": playstation_games,
            "xbox_games": xbox_games,
            "switch_games": switch_games,
        }


        return render(request, template, context)


    def post(self, request):
        ...


class GameDetailView(View):
    '''view a specific game'''

    def get(self, request, id):
        game = Game.objects.get(id=id)
        template = 'game_detail.html'
        context = {'game': game}

        return render(request, template, context)


    def post(self, request):
        ...



class CreateGameView(View):
    '''can create a review on a game in db'''

    def get(self, request):
        template = 'generic_form.html'
        form = CreateGameForm()
        context = {'form': form}
        return render(request, template, context)


    def post(self, request):
        form = CreateGameForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            game = Game.objects.create(
                name = data['name'],
                slug = data['slug'],
                rating = data['rating'],
                platfom = data['platfom'],
                released_at = data['released_at'],
                background_image = data['background_image'],
            )
            return redirect('/')
