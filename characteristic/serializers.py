from turtle import heading
from rest_framework import serializers

class CharacteristicSerializer(serializers.Serializer):
    uuid = serializers.IntegerField(read_only=True)
    weight = serializers.FloatField()
    height = serializers.IntegerField()
    years_old = serializers.IntegerField()
    favorite_toy = serializers.CharField(max_length=20)
    friendly = serializers.BooleanField()