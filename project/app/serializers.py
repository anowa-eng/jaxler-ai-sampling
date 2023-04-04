from rest_framework import serializers

class ConversationalDataSerializer(serializers.Serializer):
    class Meta:
        fields = ['__all__']