from django.urls import path
from faq_comment import views as faq_comment_views


urlpatterns = [
    path('create_faq_comment/<int:id>', faq_comment_views.CreateFaqComment.as_view(), name='create_faq_comment'),
]