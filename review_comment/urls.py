from django.urls import path
from review_comment import views as review_comment_views


urlpatterns = [
    path('create_review_comment/<int:id>/', review_comment_views.CreateReviewComment.as_view(), name='create_review_comment'),
    path('reply_review_comment/<int:id>/', review_comment_views.ReplyToReviewComment.as_view(), name='reply_review_comment'),
]