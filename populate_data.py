from api.models import ApiSearch
from games.models import Game
import argparse
import sys
import os


def create_parse():

    parser = argparse.ArgumentParser(
        description='Populates data base with games'
    )

    parser.add_argument('pop', help='populates db with games')
    return parser


def main(args):

    parser = create_parse()
    ns = parser.parse_args(args)

    pop = ns.pop

    if not ns:
        parser.print_usage()


    def populate():
        req = ApiSearch()
        api_games = req.get_all_games()
        for game in api_games:
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

    if pop:
        populate()

if __name__ == '__main__':
    main(sys.argv[1:])

