from rest_framework import serializers
from django.db import models




class DistributorSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    registration_date = serializers.DateField()
    designation = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    percentage = serializers.DecimalField(max_digits=5, decimal_places=2)
    prev_cumpv = serializers.DecimalField(max_digits=10, decimal_places=2)
    exclusive_pv = serializers.DecimalField(max_digits=10, decimal_places=2)
    self_pv = serializers.DecimalField(max_digits=10, decimal_places=2)
    group_pv = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_pv = serializers.DecimalField(max_digits=10, decimal_places=2)
    short_points = serializers.DecimalField(max_digits=10, decimal_places=2)
    next_level_percentage = serializers.DecimalField(max_digits=5, decimal_places=2)
    vid = serializers.CharField(max_length=255)
    upline_id = serializers.UUIDField()
    address = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=255)

