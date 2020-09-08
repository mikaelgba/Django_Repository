from rest_framework import viewsets
from . import models
from . import serializers

class HqViewset(viewsets.ModelViewSet):
    
    queryset = models.Hq.objects.all()
    serializer_class = serializers.HqSerializers