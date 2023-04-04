from rest_framework import serializers

class ConversationalDataSerializer(serializers.Serializer):
    prompt = serializers.CharField()
    response = serializers.CharField()