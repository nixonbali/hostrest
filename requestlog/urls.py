from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from requestlog.views import RequestLogViewSet

request_list = RequestLogViewSet.as_view({
    'get': 'list'
})

urlpatterns = format_suffix_patterns([
    path('', request_list, name="requestlog-list")
])
