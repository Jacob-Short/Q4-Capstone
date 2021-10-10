from django.core.management.base import BaseCommand
from games.models import Game
from api.models import ApiSearch


class Command(BaseCommand):
    help='can popluate db with api games'

    def handle(self, *args, **options):
            req = ApiSearch()
            api_games = req.get_all_games()
            try:
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
                self.stdout.write(self.style.SUCCESS("DB has been filled..."))
            except Exception as err:
                self.stdout.write(self.style.ERROR(f"Something has gone wrong...Error: [{err}]"))


