from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse
from accounts.forms import LoginForm, PostForm, SignupForm
from accounts.models import MyUser
from django.shortcuts import HttpResponseRedirect, render, reverse, redirect



class IndexView(View):
    '''homepage'''
    def get(self, request):
        template = 'index.html'
        context = {}
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
            login(request, user)
            return redirect(reverse("homepage"))


class LoginView(View):
    
    def get(self, request):
        template_name = 'generic_form.html'
        form = LoginForm()
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
                return redirect(request.GET.get("next", "/"))


def logout_view(request):
    logout(request)
    return redirect(reverse("homepage"))


class ProfileView(View):
    '''each users profile'''

    def get(self, request, id):
        template = 'profile.html'
        user = MyUser.objects.get(id=id)
        context = {'user': user}
        # breakpoint()
        return render(request, template, context)


    def post(self, request):
        ...


def edit_profile(request, id):
    profile_id = request.user.id
    profile_user = MyUser.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile_user.bio=data['bio']
            profile_user.email=data['email']
            profile_user.gamer_tag=data['gamer_tag']
            profile_user.picture=data['picture']
            profile_user.save()
            print(data['picture'])
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = PostForm(initial={
        'username': profile_user.username,
        'bio': profile_user.bio,
        'email': profile_user.email,
        'gamer_tag': profile_user.gamer_tag,
        'picture': profile_user.picture,
        })
        context = {'form': form}
        return render(request, 'profile_edit.html', context)