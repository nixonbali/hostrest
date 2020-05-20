from rest_framework import viewsets, mixins
from rest_framework.response import Response
from requestlog.models import RequestLog
from requestlog.serializers import RequestLogSerializer

class RequestLogViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):

    queryset = RequestLog.objects.all()
    serializer_class = RequestLogSerializer

    def list(self, request):
        new_entry = RequestLogSerializer(data={'type':'GET'})
        if new_entry.is_valid():
            new_entry.save()

        queryset = RequestLog.objects.all().order_by('-time')[:10]
        serializer = RequestLogSerializer(queryset, many=True, context={'request': request})

        return Response({'requests': serializer.data})
