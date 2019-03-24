from behave import *
from features.dao.api.api import Api
from features.page.home_page_page import HomePage

home_page = HomePage()

@step(u'que eu tenha informações das solicitações')
def step_impl(context):
    api = Api()
    global manifestations
    manifestations = api.get_manifestations()

@step(u'vejo a quantidade que aparece em cada aba')
def step_impl(context):
    global ammount_manifestation
    ammount_manifestation = home_page.get_number_manifestation_header()

@step(u'as informações tem que serem iguais')
def step_impl(context):
    qnt = {}
    for manifestation in manifestations:
        status = manifestation['statusManifestation']['title']
        if status not in qnt.keys():
            qnt[status] = 1
        else:
            qnt[status] += 1

    for k, v in qnt.items():
        assert int(ammount_manifestation[k]), qnt[k]