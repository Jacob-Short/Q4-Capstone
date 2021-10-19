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


from django.contrib import messages as django_messages
import smtplib
import sqlite3

# from community import settings



class IndexView(View):
    '''index to login or sign up'''
    def get(self, request):
        template = 'index.html'
        context = {}
        return render(request, template, context)


class HomePageView(LoginRequiredMixin, View):
    '''homepage'''
    def get(self, request):
        template = 'homepage.html'

        user = request.user.id
        target_user = request.user
        messages = Message.objects.filter(recipient=user)

        faqs = UserFaq.objects.all().order_by('-time_created')

        reviews = Review.objects.all()

        games = Game.objects.all()

        front_page_photos = list(Game.objects.all())

        three_games = random.sample(front_page_photos, 3)

        three_photos = []


        # can make this function into its own function
            # so can use on more pages than just homepage

        for game in three_games:
            three_photos.append((game.image_background, game.name))

        print(f'threee photos: {three_photos}')
        
        first_image = three_photos[0][0]
        first_title = three_photos[0][1]

        second_image = three_photos[1][0]
        second_title = three_photos[1][1]

        third_image = three_photos[2][0]
        third_title = three_photos[2][1]

        # checking for community
        possible_community = {}


        for game in games:
            specific_game_review_users = Review.objects.filter(game=game)
            specific_game_faq_users = UserFaq.objects.filter(game=game)
            review_users = [x.user_created for x in specific_game_review_users]
            faq_users = [x.user for x in specific_game_faq_users]
            for person in review_users:
                if person in faq_users:
                    if game not in possible_community:
                        possible_community[game] = [person]
                    else:
                        possible_community[game].append(person)
        print(possible_community)


        for key in possible_community:
            if len(possible_community[key]) > 1:
                community_game = key
                community_game_id = key.id
                possible_community_members = possible_community[key]
                print('A community is available to be created')




        message_notifications = MessageNotification.objects.filter(
        user_notified=target_user
        )
        review_notifications = ReviewNotification.objects.filter(user_notified=target_user)
        faq_notifications = MessageNotification.objects.filter(user_notified=target_user)

        all_notifications = list(message_notifications) + list(review_notifications) + list(faq_notifications)

        notifications_count = len(all_notifications)


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
            # "community_game": community_game,
            # "community_game_id": community_game_id,
            # "possible_community_members": possible_community_members,
            "notifications_count": notifications_count
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
            user = MyUser.objects.create_user(
                username=data.get("username"), password=data.get("password"),gamer_tag=data.get("gamer_tag"),email=data.get("email")
            )

            gmail_user = 'jacobshort.stu@gmail.com'
            gmail_password = 'wlkkouoagzjzzggm'


            sent_from = gmail_user
            to = user.email
            subject = 'Welcome to Gamerzone!'
            body = f'''Thank you so much for signing up with us {user.username}!'''

            email_text = f'''
            From: {sent_from}\n
            To: {to}\n
            Subject: {subject}\n
            {body}
            '''

            try:
                smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                smtp_server.ehlo()
                smtp_server.login(gmail_user, gmail_password)
                smtp_server.sendmail(sent_from, to, email_text)
                smtp_server.close()
                print ("Email sent successfully!")
                django_messages.success(request, django_messages.SUCCESS, f"Login Successful")
                login(request, user)
                return redirect(reverse("homepage"))    
            except Exception as ex:
                print ("Something went wrong….",ex)
                return redirect(reverse("homepage"))


class LoginView(View):
    
    def get(self, request):
        template_name = 'generic_form.html'
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
                django_messages.success(request, f'You have successfully logged in')
                return redirect(reverse("homepage"))
            if user is not None:
                login(request, user)
                return redirect(reverse('generic_form.html'))
            else:
                django_messages.success(request, f'Invalid credentials, please try again!')
                return redirect('login')


def logout_view(request):
    logout(request)
    django_messages.error(request, f"Logged out")
    return redirect(reverse("homepage"))


class ProfileView(View):
    '''each users profile'''

    def get(self, request, id):
        template = 'profile.html'


        target_user = MyUser.objects.get(id=id)
        communities = Community.objects.filter(members=target_user)
        messages = Message.objects.filter(recipient=target_user)

 
        message_notifications = MessageNotification.objects.filter(
        user_notified=request.user
        )
        review_notifications = ReviewNotification.objects.filter(user_notified=request.user)
        faq_notifications = MessageNotification.objects.filter(user_notified=request.user)

        all_notifications = list(message_notifications) + list(review_notifications) + list(faq_notifications)

        notifications_count = len(all_notifications)
        context = {'target_user': target_user, 'messages': messages, "notifications_count": notifications_count, 'communities': communities}
        return render(request, template, context)


    def post(self, request):
        ...


class EditProfile(View):
    '''can edit your profile'''
    def get(self, request, id):
        profile_user = MyUser.objects.get(id=id)
        form = EditProfileForm(initial={
        'username': profile_user.username,
        'bio': profile_user.bio,
        'email': profile_user.email,
        'gamer_tag': profile_user.gamer_tag,
        'picture': profile_user.picture,
        'favorite_game': profile_user.favorite_game
        })
        context = {'form': form}
        return render(request, 'profile_edit.html', context)
        
    def post(self, request, id):
        profile_id = request.user.id
        profile_user = MyUser.objects.get(id=id)
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile_user.bio=data['bio']
            profile_user.email=data['email']
            profile_user.gamer_tag=data['gamer_tag']
            profile_user.picture=data['picture']
            profile_user.favorite_game=data['favorite_game']
            profile_user.save()
            print(data['picture'])
            return HttpResponseRedirect(reverse('homepage'))



def about_devs(request):
    template = 'about_devs.html'
    user = request.user.id
    messages = Message.objects.filter(recipient=user)
    context = {"messages": messages}
    return render(request, template, context)


class SearchUsersView(View):
    '''search for users in the db by gt'''

    def post(self, request):
        form = SearchUserForm(request.POST)
        user = request.user.id
        try:
            if form.is_valid():
                data = form.cleaned_data
                gt = data['gamer_tag']
                user = MyUser.objects.get(gamer_tag=gt)

            id = user.id
            return redirect(f'/profile/{id}')
        except Exception as err:
            # need to display message to user that match is not found
                # try checking capitalization
            django_messages.error(request, f"User does not exist, try checking capitalization")
            print(err)
            return HttpResponseRedirect(reverse('homepage'))


class VirtualTour(LoginRequiredMixin, View):
    '''homepage'''
    def get(self, request):
        template = 'virtual_tour.html'

        user = request.user.id
        messages = Message.objects.filter(recipient=user)

        faqs = UserFaq.objects.all().order_by('-time_created')

        reviews = Review.objects.all()

        games = Game.objects.all()

        front_page_photos = list(Game.objects.all())

        three_games = random.sample(front_page_photos, 3)

        three_photos = []

        for game in three_games:
            three_photos.append((game.image_background, game.name))

        print(f'threee photos: {three_photos}')
        
        first_image = three_photos[0][0]
        first_title = three_photos[0][1]

        second_image = three_photos[1][0]
        second_title = three_photos[1][1]

        third_image = three_photos[2][0]
        third_title = three_photos[2][1]

        # cynthia
        engine = pyttsx3.init()
        engine.setProperty('voice', 'english_rp+f3')
        engine.say('''
        Hello and welcome to the gamerzone. Where gamers from all around the world can come to
        find and create Frequently Asked Questions, Reviews, or just chat about a game with a friend!
        ''')
        engine.runAndWait()
        engine.say('''
        Dont see a game that you like ? If you will direct your attention to the top of the screen in our navigation bar, we
        have a games section where you can add a game to our selection!
        ''')
        engine.runAndWait()
        engine.say('''
        Towards the bottom of the sreen, we have the most recent questions asked, as well as the most
        active review!
        ''')
        engine.runAndWait()
        engine.say('''
        See a question that you know the answer to ? Create a thread on that question!
        ''')
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
            "games": games
        }
        return render(request, template, context)