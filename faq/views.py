from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, reverse
from django.views.generic import View
from faq.forms import FaqForm
from faq.models import UserFaq
from games.models import Game

class CreateFaqView(View):
    
    def get(self, request, id):
        template_name = "generic_form.html"
        form = FaqForm()
        return render(request, template_name, {"form": form, "header": "Create a Post"})

    def post(self, request, id):
        form = FaqForm(request.POST)
        game = Game.objects.get(id=id)
        if form.is_valid():
            data = form.cleaned_data
            faq = UserFaq.objects.create(question=data.get("question"), user=request.user, game=game)
            return HttpResponseRedirect(reverse("homepage"))


class FaqView(View):
    
    def get(self, request):
        faqs = UserFaq.objects.all().order_by('-time_created')
        return render(request, 'faq.html', {'faqs': faqs})