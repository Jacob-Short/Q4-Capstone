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
        os.system("python manage.py populate_games")

    if pop:
        populate()

if __name__ == '__main__':
    main(sys.argv[1:])

