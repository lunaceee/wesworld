import unittest
import etsy
import mock
from model import Cache

mock_cache = mock.MagicMock()
mock_cursor = mock.MagicMock()
mock_cursor.first = mock.MagicMock(return_value=None)
mock_cache.query.filter = mock.MagicMock(return_value=mock_cursor)
mock_cached_get = mock.MagicMock(return_value=({'results':'[]'}, 200))

class TestEsty(unittest.TestCase):

    def setUp(selt):
        pass

    def tearDown(self):
        pass

    @mock.patch('etsy.Cache', mock_cache)
    def test_get_from_cache_no_results(self):
        key = "https://openapi.etsy.com/v2/listings/active?color=5B1A18&color_accuracy=10&limit=10&sort_on=score&category=clothing/shirt&api_key=w4kl15san4n93vl9sc0b01m8"
        result = etsy.get_from_cache(key)
        self.assertEqual(result, None)

    @mock.patch('etsy.Cache', mock_cache)
    def test_get_from_cache_typical_results(self):
        key = "https://openapi.etsy.com/v2/listings/active?color=5B1A18&color_accuracy=10&limit=10&sort_on=score&category=clothing/shirt&api_key=w4kl15san4n93vl9sc0b01m8"
        cache = Cache(key=key, value='{}')
        mock_cursor.first = mock.MagicMock(return_value=cache)
        result = etsy.get_from_cache(key)
        self.assertEqual(result, '{}')

    @mock.patch('etsy.cached_get', mock_cached_get)
    def test_get_results_typical(self):
        color = "FFFFFF"
        etsy_category = "clothing/shorts"
        mock_cached_get.return_value = ({'results':'[]'}, 200)
        result = etsy.get_results(color, etsy_category)
        self.assertEqual(result, '[]')

    @mock.patch('etsy.cached_get', mock_cached_get)
    def test_get_results_bad(self):
        color = "FFFFFF"
        etsy_category = "clothing/shorts"
        mock_cached_get.return_value = ({'results':'[]'}, 300)
        result = etsy.get_results(color, etsy_category)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()