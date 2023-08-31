from django.db import transaction
from rest_framework import serializers

from interview.inventory.models import Inventory, InventoryLanguage, InventoryTag, InventoryType


class InventoryTagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InventoryTag
        fields = ['id', 'name', 'is_active']
        
        
class InventoryLanguageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InventoryLanguage
        fields = ['id', 'name']


class InventoryTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InventoryType
        fields = ['id', 'name']


class InventorySerializer(serializers.ModelSerializer):
    type = InventoryTypeSerializer()
    language = InventoryLanguageSerializer()
    tags = InventoryTagSerializer(many=True)
    metadata = serializers.JSONField()
    
    class Meta:
        model = Inventory
        fields = ['id', 'name', 'type', 'language', 'tags', 'metadata']

    @staticmethod
    def _create_inventory_tags(inventory: Inventory, tags):
        inventory_tag_model = inventory.tags.through
        inventory_tags = [inventory_tag_model(inventorytag=tag, inventory=inventory) for tag in tags]
        inventory_tag_model.objects.bulk_create(inventory_tags)

    @transaction.atomic
    def create(self, validated_data):
        type_data = validated_data.pop("type")
        validated_data["type"] = InventoryType.objects.create(**type_data)

        language_data = validated_data.pop("language")
        validated_data["language"] = InventoryLanguage.objects.create(**language_data)

        tags = InventoryTag.objects.bulk_create([InventoryTag(**tag_data) for tag_data in validated_data.pop("tags")])

        instance = super().create(validated_data=validated_data)
        self._create_inventory_tags(inventory=instance, tags=tags)

        return instance
