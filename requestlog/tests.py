from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

class RequestLogTest(TestCase):
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
