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

        games = Game.objects.all()
        template = 'db_games.html'
        context = {'games': games}

        return render(request, template, context)

    def post(self, request):
        ...
