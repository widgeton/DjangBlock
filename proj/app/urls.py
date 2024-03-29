from django.urls import path

from . import views

urlpatterns = [
    path("dogs/", views.DogList.as_view(), name="dogs_list"),
    path("dogs/<int:pk>/", views.DogDetails.as_view(), name="dogs_detail"),
    path("breeds/", views.BreedList.as_view(), name="breeds_list"),
    path("breeds/<int:pk>/", views.BreedDetails.as_view(), name="breeds_detail"),
]
