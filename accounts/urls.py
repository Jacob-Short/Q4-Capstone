from django.urls import path
from accounts import views as account_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', account_views.IndexView.as_view(), name='root'),
    path('home/', account_views.HomePageView.as_view(), name='homepage'),
    path("signup/", account_views.SignUpView.as_view(), name="signup"),
    path("login/", account_views.LoginView.as_view(), name="login"),
    path("logout/", account_views.logout_view, name="logout"),
    path("profile/<int:id>/", account_views.ProfileView.as_view(), name="profile"),
    path("edit/<int:id>/", account_views.edit_profile, name="editprofile"),
    path("about_devs/", account_views.about_devs, name="about"),
    path("search_user/", account_views.SearchUsersView.as_view(), name="users"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)