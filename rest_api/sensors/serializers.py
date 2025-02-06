from rest_framework import serializers
from .models import Sensor

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'system', 'ph', 'temperature', 'tds', 'created_time']
        read_only_fields = ['created_time']

    def validate_system(self, value):
        if value.owner != self.context['request'].user:
            raise serializers.ValidationError("You do not own this system.")
        return value