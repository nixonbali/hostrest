from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

class RequestLogListTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.path = reverse("requestlog-list")

    def test_index_content_len(self):
        responses = [self.client.get(self.path) for _ in range(11)]
        response = responses[10]
        assert(len(response.data['requests']) == 10)

    def test_index_status(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, 200)

    def test_index_host_details(self):
        pass

class RequestLogDetailTest(TestCase):
    def test_api_get(self):
        self.factory = APIRequestFactory()
        self.path = 'api'
        _request = self.factory.get(reverse("requestlog-list"))
        _response = request_list(_request)
        request = self.factory.get(self.path)
        response = request_detail(request, pk=1)
        ## Status Code
        self.assertEqual(response.status_code, 200)

    def test_api_get(self):
        pass

    def test_api_post(self):
        pass

    def test_api_put(self):
        pass

    def test_api_delete(self):
        pass
