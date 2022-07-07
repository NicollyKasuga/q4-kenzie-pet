from rest_framework import serializers

class GroupsSerializer (serializers.Serializer):
    uuid= serializers.IntegerField(read_only=True)
    breed = serializers.CharField(max_length=(20))