from rest_framework import serializers


class DistributorSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField(max_length=255)
    vid = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=255)
 
    