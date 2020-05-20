from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory
from django.urls import reverse
from requestlog.urls import request_list, request_detail

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
        response = self.client.get(self.path)
        assert 'date' in response.data
        assert 'cpuinfo' in response.data


class RequestLogDetailTest(TestCase):
    def setUp(self):
        """Initializes factory and populates test db with single request"""
        self.factory = APIRequestFactory()
        self.path = 'api'
        _request = self.factory.get(reverse("requestlog-list"))
        _response = request_list(_request)

    def test_api_get_found_status(self):
        request = self.factory.get(self.path)
        response = request_detail(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_api_get_found_comment(self):
        request = self.factory.get(self.path)
        response = request_detail(request, pk=1)
        assert 'comment' in response.data
        self.assertEqual(response.data['comment'], None)

    def test_api_get_not_found(self):
        request = self.factory.get(self.path)
        response = request_detail(request, pk=2)
        self.assertEqual(response.status_code, 404)

    def test_api_post(self):
        pass

    def test_api_put(self):
        pass

    def test_api_delete(self):
        pass
