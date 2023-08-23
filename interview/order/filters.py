from rest_framework import serializers


class OrderFilterSerializer(serializers.Serializer):

    start_date__gte = serializers.DateField(required=False)

    embargo_date__lte = serializers.DateField(required=False)
