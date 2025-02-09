from rest_framework import serializers
from api.models import Bid

class BidSerializer(serializers.ModelSerializer):
    position = serializers.CharField(max_length=100)
    company = serializers.CharField(max_length=100)
    link = serializers.URLField()
    resume = serializers.URLField()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Bid
        fields = '__all__'