# Created by gledsons at 22/03/2019
#language: pt

Funcionalidade: Pagina lista de manifestacoes

  Contexto:

    Dado que estou logado no sistema

  Cenario: 1 - Validar a quantidade de solicitações na aba
    Dado que eu tenha informações das solicitações
    E vejo a quantidade que aparece em cada aba
    Então as informações tem que serem iguais
