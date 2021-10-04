from django.urls import path
from accounts import views as account_views
from accounts import views

urlpatterns = [
    path('', account_views.IndexView.as_view(), name='homepage'),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
]