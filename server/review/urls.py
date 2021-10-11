from django.urls import path
from review import views as review_views


urlpatterns = [
    path('create_review/', review_views.CreateReview.as_view(), name='create_review'),
    path('reviews/', review_views.Reviews.as_view(), name='reviews'),

]