from features.utils.web_app import webapp
from features.utils.wait import Wait
import re

class HomePage(object):

    def __init__(self):
        self.title_home_page = "main__header__title"
        self.header_ammount_manifestation = "filter__list"

        self.driver = webapp.get_driver()

    def check_home_page(self):
        wait = Wait()
        wait.expect_visible_class(self.title_home_page)

    def get_number_manifestation_header(self):
        ammount = self.driver.find_element_by_class_name(self.header_ammount_manifestation)
        values = ammount.find_elements_by_class_name('filter__list__item')
        data = {}
        for value in values:
            name_key = re.sub('[0-9]', '', value.text)
            data[name_key] = value.find_element_by_class_name('filter__value').text

        return data
