from django.db import models
import random

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

    
    def get_three_games(self):
        '''returns 3 random images'''
        url = self.apiurl + f'/games?key={TOKEN}'
        response = self.session.get(url)
        data = response.json()
        res = data['results']

        three_photos = []
        def main():
            max = len(res)
            for _ in range(3):
                ran = random.randint(0, max)
                three_photos.append(((res[ran]['background_image']), (res[ran]['name'])))



            print(three_photos)

        try:
            main()
        except Exception as err:
            print(err)
            main()

        return three_photos


    def search_one_game(self, slug):
        url = self.apiurl + f'games/{slug}?key={TOKEN}'
        response = self.session.get(url)
        data = response.json()
        return data