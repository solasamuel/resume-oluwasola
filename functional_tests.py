from selenium import webdriver
from django.urls import reverse
import unittest



class NewUserTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_navigate_the_site(self):
        # Dan is looking to recruit a software developer to work on his app idea.
        # He has heard about Sola and goes to check out his homepage
        self.browser.get('http://localhost:8000')

        # He recognizes sola's name in the page title and header
        self.assertIn('Sola Samuel | oluwasolasamuel4@gmail.com',
                      self.browser.title)

        # He sees the home page and the navigation menu
        html = self.browser.page_source
        assert '<a href="%s">Home</a>' % '/' in html
        assert '<a href="%s">Resume</a>' % '/resume/' in html
        assert '<a href="%s">Blog</a>' % '/blog/' in html
        assert '<a href="%s">Contact</a>' % '/contact/' in html
        self.fail('Finish the test!')

        # He wants to contact sola
        # [...rest of comments as before]


if __name__ == '__main__':
    unittest.main(warnings='ignore')
