from rest_framework import serializers
from requestlog.models import RequestLog

class RequestLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RequestLog
        fields = ['url', 'id', 'time', 'type', 'comment']
