from rest_framework.relations import SlugRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
)

from message.models import Message

class MessageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = [
            'date',
            'message',
            'author',
            'platformrecipient',
        ]