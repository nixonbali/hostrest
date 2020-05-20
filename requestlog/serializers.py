from rest_framework import serializers
from requestlog.models import RequestLog

class RequestLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RequestLog
        fields = ['url', 'id', 'time', 'type', 'comment']
        extra_kwargs = {
            'url': {'read_only': True},
            'id': {'read_only': True},
            'time': {'read_only': True},
            'type': {'read_only': True},
            'comment': {'read_only': False}
        }
