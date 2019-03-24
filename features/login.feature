# Created by gledsons at 22/03/2019
#language: pt

Funcionalidade: Login do usuario

  Cenario: 1 - Login Valido
    Dado que informo o login "gledso.santos@gmail.com"
    E senha "Teste#10"
    Quando clico em logar
    Então vejo a tela inicial

  Cenario: 2 - Login com e-mail invalido
    Dado que informo o login "gledso.santos"
    E senha "Teste#10"
    Quando clico em logar
    Então vejo a mensagem "email não possui um formato correto"

  Cenario: 3 - Login com usuario invalido
    Dado que informo o login "aaaaaa@gmail.com"
    E senha "Teste#10"
    Quando clico em logar
    Então vejo a mensagem "E-mail ou senha incorreto"
