from django.shortcuts import render, redirect
from django.views.generic import View

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
        ...


    def post(self, request):

        def populate(self, reuqest):

            # conn = sqlite3.connect("the-portal.db")

            # c = conn.cursor()

            # c.execute(
            #     """
            #     CREATE TABLE IF NOT EXISTS games (
            #         ID INTEGER PRIMARY KEY AUTOINCREMENT,
            #         name VARCHAR(150) NOT NULL,
            #         password VARCHAR(150) NOT NULL,
                    
            #     )
            #     """
            # )
