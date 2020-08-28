from rest_framework import serializers

from .models import IDE


class IDESerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IDE
        fields = ('title', 'code', 'inp', 'output')
