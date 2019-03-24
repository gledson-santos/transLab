from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from features.utils.web_app import webapp
from time import sleep


class Wait(object):

    def __init__(self):
        self.driver = webapp.get_driver()
        self.wait = WebDriverWait(self.driver, 5)

    def expect_visible_class(self, element):
        attempt = 0
        while True:
            element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, element)))
            attempt += 1
            if element is not None or attempt > 3:
                return
            sleep(1)