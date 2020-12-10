import unittest
from webdriver import Driver
from values import strings
from pageobjects.homescreen import HomeScreen

class TestExample(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_home_screen_component(self):
        home_screen = HomeScreen(self.driver)
        home_screen.validate_title_is_present()

    def tearDown(self):
        self.driver.instance.quit()

if __name__ == "__main__":
    unittest.main()