import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from helper_functions import get_url_from_list, is_valid_url, list_from_file

github_domain = "github.com"

class TestGithubLink(unittest.TestCase):
    def setUp(self):
        links = list_from_file()
        self.github_link = get_url_from_list(links, github_domain, "MISSING GITHUB LINK")

    @weight(0.5)
    @number(1)
    def test_github_link(self):
        self.assertTrue(is_valid_url(self.github_link), msg="GITHUB LINK DOES NOT WORK")
