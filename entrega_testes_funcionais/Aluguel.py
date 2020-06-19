# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 18:00:31 2020

@author: bruno
"""

import requests
import json

class Aluguel:
    def __init__(self, valor_nominal, dia):
        self.valor_nominal = valor_nominal
        self.dia = dia
        params = "{\"valor_nominal\":" + str(valor_nominal) + ",\"dia\":" + str(dia) + "}"
        self.API_URL = "https://aluguebug.herokuapp.com/calc?dados="+params

    def calcula_valor(self):
        response = requests.get(self.API_URL)
        result = json.loads(response.json())
        return result
