from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.views.generic import View
from api.models import ApiSearch
from message.models import Message
from games.models import Game
from games.forms import CreateGameForm, SearchGameForm
from django.contrib import messages as django_messages
from message_notification.models import MessageNotification
from review_notification.models import ReviewNotification
from faq_notification.models import FaqNotification

from all_notifications.views import get_notification_count

import random


def filtered_games(request, games):
    template = "games.html"
    user = request.user.id
    messages = Message.objects.filter(recipient=user)
    message_notifications = MessageNotification.objects.filter(user_notified=user)
    review_notifications = ReviewNotification.objects.filter(user_notified=user)
    faq_notifications = MessageNotification.objects.filter(user_notified=user)
    all_notifications = (
        list(message_notifications)
        + list(review_notifications)
        + list(faq_notifications)
    )
    notifications_count = len(all_notifications)
    context = {
        "games": games,
        "messages": messages,
        "notifications_count": notifications_count,
    }
    return render(request, template, context)


class GamesHomeView(View):
    """view alll games in db"""

    def get(self, request):
        form = SearchGameForm()
        all_games = [game for game in Game.objects.all()]

        games = random.sample(all_games, 250)
        template = "games.html"
        user = request.user.id
        messages = Message.objects.filter(recipient=user)

        message_notifications = MessageNotification.objects.filter(user_notified=user)
        review_notifications = ReviewNotification.objects.filter(user_notified=user)
        faq_notifications = MessageNotification.objects.filter(user_notified=user)
        all_notifications = (
            list(message_notifications)
            + list(review_notifications)
            + list(faq_notifications)
        )
        notifications_count = len(all_notifications)

        context = {
            "form": form,
            "games": games,
            "messages": messages,
            "notifications_count": notifications_count,
        }

        return render(request, template, context)

    def post(self, request):
        form = SearchGameForm(request.POST)
        user = request.user.id
        all_game_names = [game.name for game in Game.objects.all()]
        message_notifications = MessageNotification.objects.filter(user_notified=user)
        review_notifications = ReviewNotification.objects.filter(user_notified=user)
        faq_notifications = MessageNotification.objects.filter(user_notified=user)
        all_notifications = (
            list(message_notifications)
            + list(review_notifications)
            + list(faq_notifications)
        )
        notifications_count = len(all_notifications)
        messages = Message.objects.filter(recipient=user)
        print(all_game_names)
        if form.is_valid():
            data = form.cleaned_data
            game = data["search"]
            if game in all_game_names:
                print(game)
                # if title.lower() == game.lower():
                games = Game.objects.filter(name__icontains=game)
                context = {
                    "form": form,
                    "games": games,
                    "messages": messages,
                    "notifications_count": notifications_count,
                }
                return render(request, "games.html", context)
            else:
                django_messages.success(
                    request, django_messages.SUCCESS, f"Sorry!, Case Sensitive!"
                )
                return redirect("/games/")


class GameDetailView(View):
    """view a specific game"""

    def get(self, request, id):
        game = Game.objects.get(id=id)

        template = "game_detail.html"
        target_user = request.user.id
        messages = Message.objects.filter(recipient=target_user)
        notifications_count = get_notification_count(request.user)
        context = {
            "game": game,
            "notifications_count": notifications_count,
            "messages": messages,
        }

        return render(request, template, context)

    def post(self, request):
        ...


class CreateGameView(View):
    """can create a review on a game in db"""

    def get(self, request):
        template = "create_game.html"
        form = CreateGameForm()
        target_user = request.user.id
        messages = Message.objects.filter(recipient=target_user)
        notifications_count = get_notification_count(request.user)
        context = {
            "form": form,
            "messages": messages,
            "notifications_count": notifications_count,
        }
        return render(request, template, context)

    def post(self, request):
        form = CreateGameForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            game = Game.objects.create(
                name=data["name"],
                slug=data["slug"],
                rating=data["rating"],
                platform=data["platform"],
                released_at=data["released_at"],
                image_background=data["image_background"],
            )
            return HttpResponseRedirect(reverse("homepage"))
        else:
            print("form is not clean")
