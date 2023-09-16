from rest_framework import serializers


class SymptomSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    title = serializers.CharField(default=None)
    path = serializers.CharField(default=None)
    disease_id = serializers.UUIDField(default=None, required=False)
    speciality_id = serializers.UUIDField(default=None, required=False)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()