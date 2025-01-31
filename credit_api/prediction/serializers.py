from rest_framework import serializers

class CreditworthinessSerializer(serializers.Serializer):
  Recency = serializers.IntegerField()
  Frequency = serializers.IntegerField()
  Monetary = serializers.FloatField()
  Stability = serializers.IntegerField()

