from django.shortcuts import render
from django.views.generic import View
from api.models import ApiSearch
from api.forms import SearchApiForm


class ApiHomeView(View):
    '''homepage for api'''

    def get(self, request):
        form = SearchApiForm()
        template = 'api_homepage.html'
        initial_search = ApiSearch()
        all_games = initial_search.get_all_games()

        results = all_games['results']
        print(results)

        context = {'results': results, 'form': form}
        return render(request, template, context)


    def post(self, request):
        ...