from django.shortcuts import redirect, render, reverse, HttpResponseRedirect
from django.views.generic import View

from .models import Community, CommunityMessage
from games.models import Game
from .forms import CreateCommunityForm, CreateCommunityMessageForm
from message.views import get_messages_count
from all_notifications.views import get_notification_count
from message.models import Message
import sqlite3


class AbilityToCreateCommunity(View):
    """when 2 or more users leave a review and faq on the same
    game, a community will then become available to create"""

    def get(self, request, id):
        """checking if a community is available"""
        conn = sqlite3.connect("db.sqlite3")
        c = conn.cursor()
        c.execute(
            """
            SELECT username FROM accounts_myuser
            WHERE 
        """
        )

    def post(self, request, id):
        ...


class CreateCommunity(View):
    """when 2 or more users leave a review and faq on the same
    game, a community will then become available to create"""

    def get(self, request):
        template = "generic_form.html"
        form = CreateCommunityForm()
        context = {"form": form}
        return render(request, template, context)

    def post(self, request):
        form = CreateCommunityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            community = Community.objects.create(
                creator=request.user,
                game=data["game"],
            )
            community.members.set(data["members"])
            return HttpResponseRedirect(reverse("homepage"))


class CommunityView(View):
    """when 2 or more users leave a review and faq on the same
    game, a community will then become available to create"""

    def get(self, request, id):
        template = "community.html"
        messages = Message.objects.filter(recipient=request.user)
        form = CreateCommunityMessageForm()
        community = Community.objects.get(id=id)
        community_messages = CommunityMessage.objects.filter(community=community).order_by("-id")

        notifications_count = get_notification_count(request.user)

        context = {
            "community": community,
            "form": form,
            "community_messages": community_messages,
            "notifications_count": notifications_count,
            "messages": messages
        }
        return render(request, template, context)

    def post(self, request, id):
        form = CreateCommunityMessageForm(request.POST)
        community = Community.objects.get(id=id)
        if form.is_valid():
            data = form.cleaned_data
            message = CommunityMessage.objects.create(
                message=data["message"], author=request.user, community=community
            )
            # community.messages.set(message)
            return HttpResponseRedirect(reverse("community", args=(id,)))
