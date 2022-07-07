from rest_framework import serializers
from characteristic.models import Characteristic
from characteristic.serializers import CharacteristicSerializer
from groups.models import Groups
from groups.serializers import GroupsSerializer
from animals.models import Animals

class AnimalSerializer(serializers.Serializer):
    uuid = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    characteristic = CharacteristicSerializer()
    group = GroupsSerializer()

    def create(self, validated_data):
        characteristic_data = validated_data.pop("characteristic")
        group_data = validated_data.pop("group")
        breed = group_data['breed']
        groups, _ = Groups.objects.get_or_create(breed)
        print(groups)
        characteristic = Characteristic.objects.create(**characteristic_data)
        animal  = Animals.objects.create(**validated_data, group=groups, characteristic=characteristic)

        return animal

    def update(self, instance: Animals, validated_data: dict):
        group_data = validated_data.pop("group")
        characteristic_data = validated_data.pop("characteristic")

        print(instance)
        # if group_data:
        #     for key, value in group_data.items():
        #         setattr(instance.group, key, value)

        # if characteristic_data:
        #     for key, value in characteristic_data.items():
        #         setattr(instance.characteristic, key, value)

        for key, value in validated_data.items():
            setattr(instance, key, value)
            instance.save()

        return instance

