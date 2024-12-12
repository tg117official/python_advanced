import unittest

import requests
from unittest.mock import patch
import asyncio

async def async_fetch_data(url):
    await asyncio.sleep(1)  # Simulates delay
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Failed to fetch data")

class TestAsyncFunction(unittest.IsolatedAsyncioTestCase):
    @patch("requests.get")
    async def test_async_fetch_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"data": "value"}
        result = await async_fetch_data("https://example.com")
        self.assertEqual(result, {"data": "value"})