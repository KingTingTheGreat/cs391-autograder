import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from helper_functions import get_url_from_list, is_valid_url

github_domain = "github.com"

class TestGithubLink(unittest.TestCase):
    def setUp(self):
        with open("/autograder/source/test.txt", "r") as f:
            text = f.read().strip()
            links = text.split()
            self.github_link = get_url_from_list(links, github_domain, "MISSING GITHUB LINK")

    @weight(50)
    @number(1)
    def test_github_link(self):
        self.assertTrue(is_valid_url(self.github_link), msg="GITHUB LINK DOES NOT WORK")
