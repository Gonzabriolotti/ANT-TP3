from .models import Cupones
from rest_framework import serializers


class CuponesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cupones
        fields = ('id','code','valid_from','valid_to','discount','active')