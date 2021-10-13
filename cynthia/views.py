from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View

class CynthiaView(View):
    '''gives a quick tour of website'''

    def get(self, request):
        return HttpResponse("Avtivate for a Tour")


    def post(self, request):
        ...


def cynthia_view(request):
    return HttpResponse("Avtivate for a Tour")