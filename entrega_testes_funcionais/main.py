# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 18:24:44 2020

@author: bruno
"""

from Aluguel import Aluguel

aluguel = Aluguel(300.0, 10)

valor_aluguel = aluguel.calcula_valor()

print('''
      Aluguebug API - FATEC \n 
      Bruno Gabriel Dionisio Faria \n 
      Valor do aluguel calculado: \n''' + str(valor_aluguel))

