import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from helper_functions import get_url_from_list, is_valid_url, list_from_file

vercel_domain = "vercel.app"

class TestVercelLink(unittest.TestCase):
    def setUp(self):
        links = list_from_file()
        self.vercel_link = get_url_from_list(links, vercel_domain, "MISSING VERCEL LINK")

    @weight(0.5)
    @number(1)
    def test_vercel_link(self):
        self.assertTrue(is_valid_url(self.vercel_link), msg="VERCEL LINK DOES NOT WORK")
