from django.urls import path
from animals.views import AnimalIDView, AnimalsView

urlpatterns = [
    path("animals/", AnimalsView.as_view()),
    path("animals/<int:animal_uuid>/", AnimalIDView.as_view())
]