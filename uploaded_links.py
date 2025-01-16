import unittest
from urllib.parse import urlparse
from requests import get

vercel_domain = "vercel.app"
github_domain = "github.com"

def is_valid_url(url) -> bool:
    res = get(url)
    return res.ok

class UploadedLinks(unittest.TestCase):
    def setUp(self):
        self.vercel_link = "https://cs391-url-shortener.vercel.app/"
        self.github_link = "https://github.com/KingTingTheGreat/top-fetch"

    def test_vercel_link(self):
        parsed_url = urlparse(self.vercel_link)
        self.assertEqual(parsed_url.hostname, vercel_domain)
        self.assertTrue(is_valid_url(self.vercel_link))

    def test_github_link(self):
        parsed_url = urlparse(self.github_link)
        self.assertEqual(parsed_url.hostname, github_domain)
        self.assertTrue(is_valid_url(self.github_link))
