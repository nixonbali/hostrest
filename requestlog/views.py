from rest_framework import viewsets, mixins
from rest_framework.response import Response
from requestlog.models import RequestLog
from requestlog.serializers import RequestLogSerializer
import subprocess

class RequestLogViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):

    queryset = RequestLog.objects.all()
    serializer_class = RequestLogSerializer

    def list(self, request):

        ## Logs Request
        new_entry = RequestLogSerializer(data={'type':'GET'})
        if new_entry.is_valid():
            new_entry.save()

        ## Host Info
        date = subprocess.getoutput("date")
        cpuinfo = subprocess.run(["cat", "/proc/cpuinfo"], capture_output=True).stdout.decode('utf-8')
        ## Dictify / Jsonify cpuinfo
        try:
            cpuinfo = { key.strip(): val.strip() \
                        for key, val in \
                        (line.split(":") for line in \
                        cpuinfo.splitlines() if line) }
        except:
            cpuinfo = cpuinfo

        ## QuerySet
        queryset = RequestLog.objects.all().order_by('-time')[:10]
        serializer = RequestLogSerializer(queryset, many=True, context={'request': request})

        return Response({'requests': serializer.data, 'date': date, 'cpuinfo': cpuinfo})
