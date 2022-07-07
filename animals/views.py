from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status

from animals.models import Animals
from animals.serializers import AnimalSerializer

class AnimalsView(APIView):

    def get(self, _:Request):
        animals: list[Animals] = Animals.objects.all()

        serialized = AnimalSerializer(instance=animals, many=True)

        return Response({"Animals": serialized.data}, status.HTTP_200_OK)

    def post(self, request:Request):
        serialized = AnimalSerializer(data=request.data)

        serialized.is_valid(raise_exception=True)

        serialized.save()
        return Response(serialized.data, status.HTTP_201_CREATED)

class AnimalIDView(APIView):

    def get(self, _:Request, animal_uuid):
        try:
            animal = get_object_or_404(Animals, pk=animal_uuid)
            serialized = AnimalSerializer(animal)

            return Response(serialized.data, status.HTTP_200_OK)
        except Http404:
            return Response({"error":"Animal not found"}, status.HTTP_404_NOT_FOUND)

    def patch(self, request:Request, animal_uuid):
        try:
            animal = get_object_or_404(Animals, pk=animal_uuid)
            serialized = AnimalSerializer(instance=animal, data=request.data)
            serialized.is_valid(raise_exception=True)
            serialized.save()
            
            return Response(serialized.data, status.HTTP_200_OK)
        except Http404:
            return Response({"erro":"Animal not found"}, status.HTTP_404_NOT_FOUND)
        

    def delete(self, _:Request, animal_uuid:int):
        try:
            animal = get_object_or_404(Animals, pk=animal_uuid)
            animal.delete()

            serialied = AnimalSerializer(animal)

            return Response(serialied.data, status.HTTP_200_OK)
        except Http404:
            return Response({"error": "Animal not found"}, status.HTTP_404_NOT_FOUND)

