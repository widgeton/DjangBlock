from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register("dogs", views.DogListViewSet, basename="dog_list")
router.register("dogs", views.DogDetailViewSet, basename="dog_detail")

urlpatterns = [
    path("", include(router.urls)),
    path("breeds/", views.BreedList.as_view(), name="breed_list"),
    path("breeds/<int:pk>/", views.BreedDetail.as_view(), name="breed_detail"),
]
