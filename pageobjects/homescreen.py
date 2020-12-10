from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from values import strings


class HomeScreen:
    def __init__(self, driver):
        self.driver = driver

        self.title = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "site-title")))

    def validate_title_is_present(self):
        assert self.title.is_displayed()