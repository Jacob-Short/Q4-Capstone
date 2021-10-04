from django.shortcuts import render
from django.views.generic import View

class IndexView(View):
    '''homepage'''
    def get(self, request):
        template = 'index.html'
        context = {}
        return render(request, template, context)