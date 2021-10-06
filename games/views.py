from django.shortcuts import render, redirect
from django.views.generic import View

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

