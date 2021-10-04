from django.db import models

from requests import Session

API = "https://api.rawg.io/api/games?key=b6a35b94fc574ae78750e6834e5e5e34"
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
        url = self.apiurl
        response = self.session.get(url)
        data = response.json()
        return data



# game = ApiSearch()
# instance = game.get_all_games()
# print(instance)
