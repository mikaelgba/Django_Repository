from rest_framework import serializers
from .models import HQ


class HQSerializer(serializers.ModelSerializer):

    class Meta:
        model = HQ
        #fields = ['id','name_hq','author','publishing_company']
        fields = '__all__'
