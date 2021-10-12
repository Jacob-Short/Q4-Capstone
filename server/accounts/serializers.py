from rest_framework.relations import SlugRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
)

from rest_framework.views import APIView

from accounts.models import MyUser

class MyUserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = [
            'gamer_tag',
            'email',
            'picture',
            'bio',
        ]


class CreateMyUserSerializer(HyperlinkedIdentityField):
    ...

class CreateMyUserSerializer(APIView):
    class Meta:
        model = MyUser
        fields = [
            'gamer_tag',
            'email',
            'picture',
            'bio',
        ]