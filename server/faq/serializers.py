from rest_framework.relations import SlugRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
)

from faq.models import UserFaq

class UserFaqSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UserFaq
        fields = [
            'user',
            'email',
            'time_created',
            'game',
            'question',
        ]