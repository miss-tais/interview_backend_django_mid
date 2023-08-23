from rest_framework import serializers


class InventoryFilterSerializer(serializers.Serializer):

    created_at__gte = serializers.DateTimeField(required=False, input_formats=['%Y-%m-%d'])
