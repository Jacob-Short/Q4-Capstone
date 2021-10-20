from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, reverse
from django.views.generic import View
from faq.forms import FaqForm
from faq.models import UserFaq
from games.models import Game
from message.models import Message
from faq_comment.models import FaqComment

from community import settings

class CreateFaqView(View):
    
    def get(self, request, id):
        target_user = request.user.id
        messages = Message.objects.filter(recipient=target_user)
        template_name = "generic_form.html"
        form = FaqForm()
        return render(request, template_name, {'messages': messages, "form": form, "header": "Create a Post"})

    def post(self, request, id):
        form = FaqForm(request.POST)
        game = Game.objects.get(id=id)
        if form.is_valid():
            data = form.cleaned_data
            faq = UserFaq.objects.create(question=data.get("question"), user=request.user, game=game)
            if game not in settings.faq_users:
                settings.faq_users[game] = [request.user.username]
            else:
                settings.faq_users[game].append(request.user.username)

            return HttpResponseRedirect(reverse("homepage"))


class FaqView(View):
    
    def get(self, request):
        faqs = UserFaq.objects.all().order_by('-time_created')
        return render(request, 'faq.html', {'faqs': faqs})


class FaqDetailView(View):

    def get(self, request, id):
        faq = UserFaq.objects.get(id=id)
        comments = FaqComment.objects.filter(faq=faq)

        template = 'faq_detail.html'
        context = {'faq': faq, 'comments': comments}
        return render(request, template, context)