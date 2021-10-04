from django.db import models

from requests import Session

API = "https://api.rawg.io/api"
TOKEN = "b6a35b94fc574ae78750e6834e5e5e34"

class ApiSearch():
    """searches api for games"""
    def __init__(self):
        self.apiurl = API
        self.headers = {
            "Accepts": "application/json",
        }
        self.session = Session()
        self.session.headers.update(self.headers)


    def get_all_games(self):
        '''gets a list of all games in db'''
        url = self.apiurl + f'/games?key={TOKEN}'
        response = self.session.get(url)
        data = response.json()
        return data


    def search_one_game(self, slug):
        url = self.apiurl + f'games/{slug}?key={TOKEN}'
        response = self.session.get(url)
        data = response.json()
        return data