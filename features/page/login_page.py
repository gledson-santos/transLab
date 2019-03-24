from features.utils.web_app import webapp


class LoginPage(object):

    def __init__(self):
        self.email_login = "email"
        self.password = "password"
        self.button_login = "btn"
        self.notification_error = "form-notification--error"

        self.driver = webapp.get_driver()

    def set_login(self, login):
        self.driver.find_element_by_id(self.email_login).send_keys(login)

    def set_password(self, password):
        self.driver.find_element_by_id(self.password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_class_name(self.button_login).click()

    def get_message_notification_erro(self):
        return self.driver.find_element_by_class_name(self.notification_error).text


