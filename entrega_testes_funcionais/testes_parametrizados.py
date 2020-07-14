# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:59:49 2020

@author: bruno
"""

import pytest
import sys
import os
import inspect
from Aluguel import Aluguel

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

parentdir = os.path.dirname(currentdir)

sys.path.insert(0, parentdir)

VALOR_NOMINAL = 300.0
DADOS_TESTES = [(0,-1), (1,270.0), (2,270.0), (5,270.0),(6,285.0),
          (7,285.0),(8,285.0),(10,285.0),(11,300.0),(14,300.0),
          (15,300.0),(16,306.3),(20,307.5),(30,310.5),(31,-1)]

### Parametrizando os testes
@pytest.mark.parametrize('dia, valor_esperado', DADOS_TESTES)
def testes(dia, valor_esperado):
    aluguel = Aluguel(VALOR_NOMINAL, dia)
    
    resultado = aluguel.calcula_valor()
    
    valor_aluguel = resultado['valor_calculado']
    
    sys.stderr.write("Dia {} - Valor esperado: {} - valor recebido: {}"
                     .format(dia, valor_esperado, valor_aluguel))
    
    assert valor_aluguel == valor_esperado