from rest_framework import views, viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Breed, Dog
from .serializers import BreedSerializer, DogListRetrieveSerializer, DogCreateUpdateSerializer


class BreedList(views.APIView):
    def get(self, request, format=None):
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BreedDetail(views.APIView):
    def get_object(self, pk):
        try:
            return Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        breed = self.get_object(pk)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        breed = self.get_object(pk)
        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DogListViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Dog.objects.all()
        serializer = DogListRetrieveSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DogCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DogDetailViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Dog.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DogListRetrieveSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Dog.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = DogCreateUpdateSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Dog.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
