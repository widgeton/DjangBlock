from rest_framework import serializers

from .models import Breed, Dog


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"


class DogListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = "__all__"
        depth = 2


class DogCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = "__all__"
