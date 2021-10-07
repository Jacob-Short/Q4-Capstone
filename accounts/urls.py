from django.urls import path
from accounts import views as account_views
from accounts import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', account_views.IndexView.as_view(), name='homepage'),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/<int:id>/", views.ProfileView.as_view(), name="profile"),
    path("edit/<int:id>/", views.edit_profile, name="editprofile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)