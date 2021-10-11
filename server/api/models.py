from django.db import models
import random

from requests import Session

API = "https://api.rawg.io/api"
TOKEN = "b6a35b94fc574ae78750e6834e5e5e34"

SECOND_API = 'https://videogamesapi.herokuapp.com'

class ApiSearch():
    """retrievs 20 api from games"""
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
        res = data["results"]
        return res

    
    def get_three_games(self):
        '''returns 3 random images'''
        url = self.apiurl + f'/games?key={TOKEN}'
        response = self.session.get(url)
        data = response.json()
        res = data['results']

        three_photos = []
        def get_random():
            max = len(res)
            for _ in range(3):
                ran = random.randint(0, max)
                three_photos.append(((res[ran]['background_image']), (res[ran]['name'])))

            # print(three_photos)

        try:
            get_random()
        except Exception as err:
            print(err)
            get_random()

        return three_photos


    def search_one_game(self, slug):
        print(type(slug))
        url = self.apiurl + f'/games/{slug}?key={TOKEN}'
        response = self.session.get(url)
        data = response.json()
        print(data)
        return data


class SecondApiSearch():
    '''retrieves 28 games from api'''
    def __init__(self):
        self.apiurl = SECOND_API
        self.session = Session()
        

    def get_first_page(self):
        url = self.apiurl + '/api/games/'
        response = self.session.get(url)
        data = response.json()['results']

        return data

    def get_second_page(self):
        url = self.apiurl + '/api/games/?page=2'
        response = self.session.get(url)
        data = response.json()['results']

        return data

    def get_third_page(self):
        url = self.apiurl + '/api/games/?page=3'
        response = self.session.get(url)
        data = response.json()['results']

        return data


    def get_fourth_page(self):
        url = self.apiurl + '/api/games/?page=4'
        response = self.session.get(url)
        data = response.json()['results']

        return data