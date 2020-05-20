from rest_framework import viewsets, mixins
from requestlog.models import RequestLog
from requestlog.serializers import RequestLogSerializer

class RequestLogViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):

    queryset = RequestLog.objects.all()
    serializer_class = RequestLogSerializer
