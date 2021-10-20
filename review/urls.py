from django.urls import path
from review import views as review_views


urlpatterns = [
    path('create_review/<int:id>/', review_views.CreateReview.as_view(), name='create_review'),
    path('reviews/', review_views.Reviews.as_view(), name='reviews'),
    path('review_detail/<int:id>/', review_views.ReviewDetailView.as_view(), name='review_detail'),
    path('delete_review/<int:id>/', review_views.delete_review, name='delete_review'),
    

]