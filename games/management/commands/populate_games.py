from django.core.management.base import BaseCommand
from games.models import Game
from api.models import ApiSearch, SecondApiSearch


class Command(BaseCommand):
    help='can popluate db with api games'

    def handle(self, *args, **options):
            req = ApiSearch()
            api_games = req.get_all_games()

            second_req = SecondApiSearch()

            page_one = second_req.get_first_page()
            page_two = second_req.get_second_page()
            page_three = second_req.get_third_page()
            page_four = second_req.get_fourth_page()

            try:
                for game in api_games:
                    populated_game = Game.objects.create(
                        name = game['name'],
                        slug = game['slug'],
                        rating = game['rating'],
                        platform = game['platforms'],
                        released_at = game['released'],
                        image_background = game['background_image'],
                    )

                for w in page_one:
                    populated_game = Game.objects.create(
                        name = w['title'],
                        slug = w['title'],
                        # rating = None,
                        # platform = w['platform'],
                        released_at = w['release_date'],
                        image_background = w['cover'],
                    )
                
                
                for x in page_two:
                    populated_game = Game.objects.create(
                        name = x['title'],
                        slug = x['title'],
                        # rating = None,
                        platform = x['platform'],
                        released_at = x['release_date'],
                        image_background = x['cover'],
                    )


                for y in page_three:
                    populated_game = Game.objects.create(
                        name = y['title'],
                        slug = y['title'],
                        # rating = None,
                        platform = y['platform'],
                        released_at = y['release_date'],
                        image_background = y['cover'],
                    )

                
                for z in page_four:
                    populated_game = Game.objects.create(
                        name = z['title'],
                        slug = z['title'],
                        # rating = None,
                        platform = z['platform'],
                        released_at = z['release_date'],
                        image_background = z['cover'],
                    )


                self.stdout.write(self.style.SUCCESS("DB has been filled..."))
            except Exception as err:
                self.stdout.write(self.style.ERROR(f"Something has gone wrong...Error: [{err}]"))


