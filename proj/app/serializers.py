from rest_framework import serializers

from .models import Breed, Dog


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"


class DogPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return f"{instance.name}"


class DogSerializer(serializers.ModelSerializer):
    breed = DogPrimaryKeyRelatedField(queryset=Breed.objects.all())

    class Meta:
        model = Dog
        fields = ("name", "age", "gender", "color", "favorite_food", "favorite_toy", "breed")
        depth = 1
