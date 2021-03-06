from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse
from accounts.forms import LoginForm, EditProfileForm, SignupForm, SearchUserForm
from accounts.models import MyUser
import community
import faq
from message.models import Message
from django.shortcuts import HttpResponseRedirect, render, reverse, redirect
from api.models import ApiSearch

from django.contrib.auth.mixins import LoginRequiredMixin

from message_notification.models import MessageNotification
from review_notification.models import ReviewNotification
from faq_notification.models import FaqNotification

from faq import views as faq_views
from review import views as review_views
from faq.models import UserFaq
from review.models import Review
from games.models import Game
from community.models import Community
import random

import pyttsx3


from django.contrib import messages
import smtplib
import sqlite3

from all_notifications.views import get_notification_count

# from community import settings


class IndexView(View):
    """index to login or sign up"""

    def get(self, request):
        template = "index.html"
        context = {}
        return render(request, template, context)


class HomePageView(LoginRequiredMixin, View):
    """homepage"""

    def get(self, request):
        template = "homepage.html"

        user = request.user.id
        target_user = request.user
        user_messages = Message.objects.filter(recipient=user)

        faqs = UserFaq.objects.all().order_by("-time_created")

        reviews = Review.objects.all()

        games = [game for game in Game.objects.all()]

        random_games = random.sample(games, 25)

        front_page_photos = list(Game.objects.all())

        three_games = random.sample(front_page_photos, 3)

        three_photos = []

        # can make this function into its own function
        # so can use on more pages than just homepage

        for game in three_games:
            three_photos.append((game.image_background, game.name))

        print(f"threee photos: {three_photos}")

        first_image = three_photos[0][0]
        first_title = three_photos[0][1]

        second_image = three_photos[1][0]
        second_title = three_photos[1][1]

        third_image = three_photos[2][0]
        third_title = three_photos[2][1]

        # checking for community
        # possible_community = {}

        # for game in games:
        #     specific_game_review_users = Review.objects.filter(game=game)
        #     specific_game_faq_users = UserFaq.objects.filter(game=game)
        #     review_users = [x.user_created for x in specific_game_review_users]
        #     faq_users = [x.user for x in specific_game_faq_users]
        #     for person in review_users:
        #         if person in faq_users:
        #             if game not in possible_community:
        #                 possible_community[game] = [person]
        #             else:
        #                 possible_community[game].append(person)
        # print(possible_community)

        # for key in possible_community:
        #     if len(possible_community[key]) > 1:
        #         community_game = key
        #         community_game_id = key.id
        #         possible_community_members = possible_community[key]
        #         print('A community is available to be created')

        message_notifications = MessageNotification.objects.filter(
            user_notified=target_user
        )
        review_notifications = ReviewNotification.objects.filter(
            user_notified=target_user
        )
        faq_notifications = MessageNotification.objects.filter(
            user_notified=target_user
        )

        all_notifications = (
            list(message_notifications)
            + list(review_notifications)
            + list(faq_notifications)
        )

        notifications_count = get_notification_count(request.user)

        context = {
            "first_image": first_image,
            "first_title": first_title,
            "second_image": second_image,
            "second_title": second_title,
            "third_image": third_image,
            "third_title": third_title,
            "user_messages": user_messages,
            "faqs": faqs,
            "reviews": reviews,
            "games": games,
            # "community_game": community_game,
            # "community_game_id": community_game_id,
            # "possible_community_members": possible_community_members,
            "notifications_count": notifications_count,
            "random_games": random_games,
        }
        return render(request, template, context)


class SignUpView(View):
    def get(self, request):
        template_name = "generic_form.html"
        form = SignupForm()
        return render(request, template_name, {"form": form, "header": "Signup"})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                user = MyUser.objects.create_user(
                    username=data.get("username"),
                    password=data.get("password"),
                    gamer_tag=data.get("gamer_tag"),
                    email=data.get("email"),
                )

                gmail_user = "jacobshort.stu@gmail.com"
                gmail_password = "wlkkouoagzjzzggm"

                sent_from = gmail_user
                to = user.email
                subject = "Welcome to Gamerzone!"
                body = f"""Thank you so much for signing up with us {user.username}!"""

                email_text = f"""
                From: {sent_from}\n
                To: {to}\n
                Subject: {subject}\n
                {body}
                """

                smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                smtp_server.ehlo()
                smtp_server.login(gmail_user, gmail_password)
                smtp_server.sendmail(sent_from, to, email_text)
                smtp_server.close()
                print("Email sent successfully!")
                messages.success(request, messages.SUCCESS, f"Login Successful")
                login(request, user)
                return redirect(reverse("homepage"))
            except Exception as ex:
                # TODO:
                # Set up logging when this fails
                print("When this happens -- Please log the error???.", ex)
                return redirect(reverse("homepage"))

        elif "email-domain" in form._errors:
            messages.add_message(request, messages.ERROR, form._errors)
            print(
                "This should be when form validation fails.. ex: [ 'domain validation' ]"
            )
            print(form._errors)
            return redirect(reverse("signup"))
        elif "existing-username" in form._errors:
            messages.add_message(request, messages.ERROR, form._errors)
            print(
                "This should be when form validation fails.. ex: [ 'UNIQUE contraint' for username ]"
            )
            print(form._errors)
            return redirect(reverse("signup"))
        elif "existing-gamer_tag" in form._errors:
            messages.add_message(request, messages.ERROR, form._errors)
            print(
                "This should be when form validation fails.. ex: [ 'UNIQUE contraint' for gamer_tag ]"
            )
            print(form._errors)
            return redirect(reverse("signup"))
        else:
            # TODO:
            # Set up logging when this fails
            messages.add_message(
                request,
                messages.ERROR,
                f"""development purposes - if this happens, please screen shot error and add 
                  description of what you did before crashing.""",
            )
            print("Something else happened")
            print(form._errors)
            return redirect(reverse("signup"))


class LoginView(View):
    def get(self, request):
        template_name = "generic_form.html"
        # INITIAL = {
        #     'username': '',
        #     'password': '',
        # }
        form = LoginForm(initial=None)
        return render(request, template_name, {"form": form, "header": "Login"})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data.get("username"), password=data.get("password")
            )
            if user:
                login(request, user)
                messages.add_message(
                    request,
                    message="You have successfully logged in.",
                    level=messages.SUCCESS,
                )
                return redirect(reverse("homepage"))
            if user is not None:
                login(request, user)
                return redirect(reverse("generic_form.html"))
            else:
                messages.add_message(
                    request, message="Invalid credentials.", level=messages.ERROR
                )
                return redirect("login")


def logout_view(request):
    logout(request)
    messages.add_message(
        request, message="You have sucessfully logged out.", level=messages.SUCCESS
    )
    return redirect(reverse("homepage"))


class ProfileView(View):
    """each users profile"""

    def get(self, request, id):
        template = "profile.html"

        target_user = MyUser.objects.get(id=id)
        communities = Community.objects.filter(members=target_user)
        user_messages = Message.objects.filter(recipient=target_user)

        notifications_count = notifications_count = get_notification_count(request.user)

        context = {
            "target_user": target_user,
            "user_messages": user_messages,
            "notifications_count": notifications_count,
            "communities": communities,
        }
        return render(request, template, context)

    def post(self, request):
        ...


class EditProfile(View):
    """can edit your profile"""

    def get(self, request, id):
        profile_user = MyUser.objects.get(id=id)
        messages = Message.objects.filter(recipient=profile_user)
        form = EditProfileForm(
            initial={
                "username": profile_user.username,
                "bio": profile_user.bio,
                "email": profile_user.email,
                "gamer_tag": profile_user.gamer_tag,
                "picture": profile_user.picture,
                "favorite_game": profile_user.favorite_game,
            }
        )
        context = {"messages": messages, "form": form, "profile_user": profile_user}
        return render(request, "profile_edit.html", context)

    def post(self, request, id):
        profile_id = request.user.id
        profile_user = MyUser.objects.get(id=id)
        form = EditProfileForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                data = form.cleaned_data
                profile_user.bio = data["bio"]
                profile_user.email = data["email"]
                profile_user.gamer_tag = data["gamer_tag"]
                profile_user.picture = data["picture"]
                profile_user.favorite_game = data["favorite_game"]
                profile_user.save()
                print(data["picture"])
                messages.add_message(
                    request,
                    message="You have sucessfully edited your profile.",
                    level=messages.SUCCESS,
                )
                return HttpResponseRedirect(reverse("profile", args=(id,)))
        except Exception as err:
            print(err)
            messages.add_message(
                request,
                message="There was an error editing your profile.",
                level=messages.ERROR,
            )
            return HttpResponseRedirect(reverse("profile", args=(id,)))


def about_devs(request):
    template = "about_devs.html"
    user = request.user.id
    user_messages = Message.objects.filter(recipient=user)

    notifications_count = get_notification_count(request.user)

    context = {
        "user_messages": user_messages,
        "notifications_count": notifications_count,
    }
    return render(request, template, context)


class SearchUsersView(View):
    """search for users in the db by gt"""

    def post(self, request):
        form = SearchUserForm(request.POST)
        user = request.user.id
        try:
            if form.is_valid():
                data = form.cleaned_data
                gt = data["gamer_tag"]
                user = MyUser.objects.get(gamer_tag=gt)

            id = user.id
            return redirect(f"/profile/{id}")
        except Exception as err:
            # need to display message to user that match is not found
            # try checking capitalization
            messages.add_message(
                request,
                message="Gamertag does not exist, try checking capitalization.",
                level=messages.INFO,
            )

            print(err)
            return HttpResponseRedirect(reverse("homepage"))


class VirtualTour(LoginRequiredMixin, View):
    """homepage"""

    def get(self, request):
        template = "virtual_tour.html"

        user = request.user.id
        messages = Message.objects.filter(recipient=user)

        faqs = UserFaq.objects.all().order_by("-time_created")

        reviews = Review.objects.all()

        games = Game.objects.all()

        front_page_photos = list(Game.objects.all())

        three_games = random.sample(front_page_photos, 3)

        three_photos = []

        for game in three_games:
            three_photos.append((game.image_background, game.name))

        print(f"threee photos: {three_photos}")

        first_image = three_photos[0][0]
        first_title = three_photos[0][1]

        second_image = three_photos[1][0]
        second_title = three_photos[1][1]

        third_image = three_photos[2][0]
        third_title = three_photos[2][1]

        # cynthia
        engine = pyttsx3.init()
        engine.setProperty("voice", "english_rp+f3")
        engine.say(
            """
        Hello and welcome to the gamerzone. Where gamers from all around the world can come to
        find and create Frequently Asked Questions, Reviews, or just chat about a game with a friend!
        """
        )
        engine.runAndWait()
        engine.say(
            """
        Dont see a game that you like ? If you will direct your attention to the top of the screen in our navigation bar, we
        have a games section where you can add a game to our selection!
        """
        )
        engine.runAndWait()
        engine.say(
            """
        Towards the bottom of the sreen, we have the most recent questions asked, as well as the most
        active review!
        """
        )
        engine.runAndWait()
        engine.say(
            """
        See a question that you know the answer to ? Create a thread on that question!
        """
        )
        engine.runAndWait()

        context = {
            "first_image": first_image,
            "first_title": first_title,
            "second_image": second_image,
            "second_title": second_title,
            "third_image": third_image,
            "third_title": third_title,
            "messages": messages,
            "faqs": faqs,
            "reviews": reviews,
            "games": games,
        }
        return render(request, template, context)


def delete_account(request, id):
    account = MyUser.objects.get(id=id)
    account.delete()
    messages.add_message(
        request,
        message="You have sucessfully deleted your account",
        level=messages.ERROR,
    )
    return redirect("/")
