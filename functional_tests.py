from selenium import webdriver
import unittest


class NewUserTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_contact_sola(self):
        # Dan is looking to recruit a software developer to work on his app idea.
        # He has heard about Sola and goes to check out his homepage
        self.browser.get('http://localhost:8000')

        # He recognizes sola's name in the page title and header
        self.assertIn('Sola Samuel | oluwasolasamuel4@gmail.com',
                      self.browser.title)
        self.fail('Finish the test!')

        # He wants to contact sola
        # [...rest of comments as before]


if __name__ == '__main__':
    unittest.main(warnings='ignore')
