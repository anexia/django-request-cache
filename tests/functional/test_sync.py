from unittest import mock

from django.test import TestCase

from django_request_cache import cache_for_request


class RequestCacheMiddlewareTest(TestCase):

    @mock.patch("testapp.views.sync.retrieve_time", spec_set=["__call__"])
    def test_sync_one_request(self, mock_func):
        cached_func = mock.MagicMock(spec_set=["__call__", "__name__"])
        mock_func.side_effect = cache_for_request(cached_func)
        self.client.get('/')
        self.assertEqual(mock_func.call_count, 2)
        self.assertEqual(cached_func.call_count, 1)

    @mock.patch("testapp.views.sync.retrieve_time", spec_set=["__call__"])
    def test_sync_two_requests(self, mock_func):
        cached_func = mock.MagicMock(spec_set=["__call__", "__name__"])
        mock_func.side_effect = cache_for_request(cached_func)
        self.client.get('/')
        self.client.get('/')
        self.assertEqual(mock_func.call_count, 4)
        self.assertEqual(cached_func.call_count, 2)

    def test_sync_pandas_dataframe(self):
        """
        Esure that the cache_for_request decorator works with pandas dataframes.
        """
        response = self.client.get('/pandas_dataframe/')
        self.assertEqual(response.status_code, 200)
