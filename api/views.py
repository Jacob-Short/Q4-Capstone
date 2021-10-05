from django.shortcuts import redirect, render
from django.views.generic import View
from api.models import ApiSearch
from api.forms import SearchApiForm

from django.contrib.auth.decorators import login_required

class ApiHomeView(View):
    """homepage for api"""

    def get(self, request):
        template = "api_homepage.html"
        initial_search = ApiSearch()
        three_photos = initial_search.get_three_games()

        first_image = three_photos[0][0]
        first_title = three_photos[0][1]

        second_image = three_photos[1][0]
        second_title = three_photos[1][1]

        third_image = three_photos[2][0]
        third_title = three_photos[2][1]

        context = {
            "first_image": first_image,
            "first_title": first_image,
            "second_image": second_image,
            "second_title": second_title,
            "third_image": third_image,
            "third_title": third_title,
        }
        return render(request, template, context)

    def post(self, request):
        ...

class ApiAllGamesView(View):
    """displaying all games in api"""

    def get(self, request):
        form = SearchApiForm()
        template = "api_all_games.html"
        initial_search = ApiSearch()
        all_games = initial_search.get_all_games()

        results = all_games
        # print(results)

        context = {"results": results, "form": form}
        return render(request, template, context)

    def post(self, request):
        template = 'api_game_detail.html'
        form = SearchApiForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            game = data['search']

            initial_search = ApiSearch()
            all_games = initial_search.get_all_games()

            for title in all_games:
                if title['name'].lower() == game.lower():
                    try:
                        data = initial_search.search_one_game(game)
                        print(title['name'])
                        print(f'data: \n {data}')
                        context = {'data': data}

                        # print(f'name: {data.name}')
                        return render(request, template, context)
                    # print(data)
                    except Exception as err:
                        print(err)
                        return redirect('/')

            


