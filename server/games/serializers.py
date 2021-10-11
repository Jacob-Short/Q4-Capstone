from rest_framework.relations import SlugRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
)

from games.models import Game

class GameSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = [
            'name',
            'slug',
            'rating',
            'platform',
            'released_at',
            'image_background',
        ]