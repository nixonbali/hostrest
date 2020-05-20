from rest_framework import viewsets, mixins, permissions, status
from rest_framework.response import Response
from requestlog.models import RequestLog
from requestlog.serializers import RequestLogSerializer
import subprocess

class RequestLogViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    """RequestLog ViewSet for Listing, Retrieving, Updating, and Deleting"""

    queryset = RequestLog.objects.all()
    serializer_class = RequestLogSerializer

    def list(self, request):
        """
        Logs new request
        Displays Host Info
        Lists 10 most recent requests
        """
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

    def update(self, request, pk=None):
        """Updates Comment or Raises 400"""
        response = super().update(request, pk)
        if ('comment' not in request.data) or \
        ('comment' not in response.data) or \
        (response.data['comment'] != request.data['comment']):
            response.status_code = status.HTTP_400_BAD_REQUEST
        return response

    def destroy(self, request, pk=None):
        """Deletes or Raises 400"""
        try:
            response = super().destroy(request, pk)
        except:
            content = {'Error': 'Cannot Remove what does not exist'}
            response = Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            response.status_code = status.HTTP_200_OK
        finally:
            return response
