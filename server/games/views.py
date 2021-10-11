from django.shortcuts import render, redirect
from django.views.generic import View
from api.models import ApiSearch
from games.models import Game

import sqlite3
import random

from rest_framework.viewsets import ModelViewSet
from games.models import Game
from games.serializers import GameSerializer


class GamesViewSet(ModelViewSet):
    '''can create a game into the database'''

    serializer_class = GameSerializer
    queryset = Game.objects.all()

    


class FillDbWithGames(View):
    '''instantiate db with games from api'''

    def get(self, request):

        games = Game.objects.all()
        template = 'db_games.html'
        context = {'games': games}

        return render(request, template, context)

    def post(self, request):
        ...
