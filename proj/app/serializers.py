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
    breed_id = serializers.IntegerField()

    class Meta:
        model = Dog
        fields = ("name", "age", "gender", "color", "favorite_food", "favorite_toy", "breed_id")

    def validate_breed_id(self, value):
        breed_ids = [breed.id for breed in Breed.objects.all()]
        if value in breed_ids:
            return value
        raise serializers.ValidationError("Wrong breed ID.")
