from rest_framework import serializers
from .models import Hq

class HqSerializers(serializers.ModelSerializer):

    class Meta:
        model = Hq
        fields ="__all__"

