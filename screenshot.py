# This Selenium script captures a screenshot, which will appear in the same directory from which you run the command to launch the script.
# It captures the entire loaded canvas - including content that's currently off-screen - which is useful if you need a screenshot of EVERYTHING on a page.
# To launch, run: python screenshot.py

import unittest
from selenium import webdriver

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_sauce(self):
        self.driver.get('http://www.instructables.com/tag/type-id/category-technology/')
        self.assertTrue("Technology" in self.driver.title);
        self.driver.get_screenshot_as_file('frontpage.png') # http://seleniumhq.org/docs/04_webdriver_advanced.html#taking-a-screenshot

    def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()