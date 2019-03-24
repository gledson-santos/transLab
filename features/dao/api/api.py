import json
import requests

class Api(object):

    def get_token(self):
        req = requests.post("https://app-node-hom.labtrans.ufsc.br/manifestacao-publica-api/authentication", data = {"email":"gledso.santos@gmail.com", "password":"Teste#10"})
        return json.loads(req.content.decode('utf-8'))

    def get_manifestations(self):
        token = self.get_token()
        token = 'Bearer ' + token['token']
        HEADERS = {"Authorization": token, "content-type": "text"}
        req = requests.get("https://app-node-hom.labtrans.ufsc.br/manifestacao-publica-api/manifestations", headers=HEADERS)
        return req.json()
