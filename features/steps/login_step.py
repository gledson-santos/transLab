from behave import *
from features.page.login_page import LoginPage
from features.page.home_page_page import HomePage

login_page = LoginPage()

@step(u'que informo o login "{usuario}"')
def step_impl(context, usuario):
    login_page.set_login(usuario)

@step(u'senha "{senha}"')
def step_impl(context, senha):
    login_page.set_password(senha)

@step(u'clico em logar')
def step_impl(context):
    login_page.click_login_button()

@step(u'vejo a tela inicial')
def step_impl(context):
    home = HomePage()
    home.check_home_page()

@step(u'vejo a mensagem "{message}"')
def step_impl(context, message):
    system_message = login_page.get_message_notification_erro()
    assert system_message, message
