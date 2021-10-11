from rest_framework.relations import SlugRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
)

from review.models import Review

class ReviewSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = [
            'rating',
            'name',
            'text',
            'game',
            'user_created',
            'time_created',
        ]