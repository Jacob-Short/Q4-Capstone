from django.urls import path
from faq import views as faq_views


urlpatterns = [
    path('faqshome/', faq_views.FaqView.as_view(), name='faqshome'),
    path('createfaq/<int:id>', faq_views.CreateFaqView.as_view(), name='createfaq'),
]