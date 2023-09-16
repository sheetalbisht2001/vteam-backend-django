from rest_framework import serializers


class DistributorSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    