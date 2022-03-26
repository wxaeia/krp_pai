from recepies.models import Receipe
from rest_framework import serializers


class ReceipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipe
        fields = '__all__'