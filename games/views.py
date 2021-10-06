from django.shortcuts import render, redirect
from django.views.generic import View
from api.models import ApiSearch
from games.models import Game

import sqlite3
import random

'''
Game:
    id, name, slug, language, games_count, image_background, 
    esbr rating, screen_shots, released at, platform

'''

class GamesHomeView(View):
    '''can view how to create a game into database'''

    def get(self, request):
        ...


    def post(self, request):
        ...



class CreateGameView(View):
    '''can create a game into the database'''

    def get(self, request):
        ...


    def post(self, request):
        ...


class FillDbWithGames(View):
    '''instantiate db with games from api'''

    def get(self, request):
       
        def populate():
            req = ApiSearch()
            api_games = req.get_all_games()
            for game in api_games:
                # print(f'each game from populate: {game}')
                populated_game = Game.objects.create(
                    name = game['name'],
                    slug = game['slug'],
                    # language = game['language'],
                    rating = game['rating'],
                    # screen_shots = game['screen_shots'],
                    platform = game['platforms'],
                    released_at = game['released'],
                    image_background = game['background_image'],
                )

        populate()
        return redirect('/')


    def post(self, request):
        ...
