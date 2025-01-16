import unittest
from urllib.parse import urlparse
from requests import get
from gradescope_utils.autograder_utils.decorators import weight, number

vercel_domain = "vercel.app"
github_domain = "github.com"

def is_valid_url(url) -> bool:
    res = get(url)
    if res.ok:
        print("url works")
    else:
        print("url does not work")
    return res.ok

class TestUploadedLinks(unittest.TestCase):
    def setUp(self):
        self.vercel_link = "https://cs391-url-shortener.vercel.app/"
        self.github_link = "https://github.com/KingTingTheGreat/top-fetch"

    @weight(50)
    @number(1)
    def test_vercel_link(self):
        parsed_url = urlparse(self.vercel_link)
        self.assertIsNot(parsed_url.hostname, None)
        if parsed_url.hostname is not None:
            self.assertTrue(parsed_url.hostname.endswith(vercel_domain), msg="checking vercel link")
        self.assertTrue(is_valid_url(self.vercel_link), msg="url works")

    @weight(50)
    @number(1)
    def test_github_link(self):
        parsed_url = urlparse(self.github_link)
        self.assertEqual(parsed_url.hostname, github_domain, msg="Checking GitHub link")
        self.assertTrue(is_valid_url(self.github_link), msg="url works")
