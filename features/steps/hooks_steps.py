from behave import *


@step(u'que estou logado no sistema')
def step_impl(context):
    context.execute_steps('''
            Dado que informo o login "gledso.santos@gmail.com"
            E senha "Teste#10"
            Quando clico em logar
            Então vejo a tela inicial                      
                          ''')