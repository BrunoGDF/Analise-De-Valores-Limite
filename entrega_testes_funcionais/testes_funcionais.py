# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 18:33:59 2020

@author: bruno
"""
import sys
from Aluguel import Aluguel

VALOR_NOMINAL = 300.0

#Testes invalidos   
def test_dia_invalido_acima_de_30_BGDF():
    aluguel = Aluguel(VALOR_NOMINAL, 31)
    valor = aluguel.calcula_valor()    
    sys.stderr.write("Esperado {} recebido {}".format(-1, valor['valor_calculado']))
    assert valor['valor_calculado'] == -1
    
def test_dia_invalido_abaixo_de_0_BGDF():
    aluguel = Aluguel(VALOR_NOMINAL, -1)
    valor = aluguel.calcula_valor()    
    sys.stderr.write("Esperado {} recebido {}".format(-1, valor['valor_calculado']))
    assert valor['valor_calculado'] == -1

#Testes do dia 1 ao dia 5
def test_dia_1_BGDF():
    aluguel = Aluguel(VALOR_NOMINAL, 1)
    valor = aluguel.calcula_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.1    
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel
    
def test_dia_2_BGDF():
    aluguel = Aluguel(VALOR_NOMINAL, 2)
    valor = aluguel.calcula_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.1    
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel
    
def test_dia_3_BGDF():
    aluguel = Aluguel(VALOR_NOMINAL, 3)
    valor = aluguel.calcula_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.1    
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel
    
def test_dia_4_BGDF():
    aluguel = Aluguel(VALOR_NOMINAL, 4)
    valor = aluguel.calcula_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.1    
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel

def test_dia_5_BGDF():
    aluguel = Aluguel(VALOR_NOMINAL, 5)
    valor = aluguel.calcula_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.1    
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel


#Testes do dia 6 ao dia 10
def test_dia_6_BGDF():
    aluguel = Aluguel(VALOR_NOMINAL, 6)
    valor = aluguel.calcula_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.05    
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel
    
def test_dia_7_BGDF():
    aluguel = Aluguel(VALOR_NOMINAL, 7)
    valor = aluguel.calcula_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.05    
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel

def test_dia_8_BGDF():
    aluguel = Aluguel(VALOR_NOMINAL, 8)
    valor = aluguel.calcula_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.05    
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel

def test_dia_9_BGDF():
    aluguel = Aluguel(VALOR_NOMINAL, 9)
    valor = aluguel.calcula_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.05    
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel
    
def test_dia_10_BGDF():
    aluguel = Aluguel(VALOR_NOMINAL, 10)
    valor = aluguel.calcula_valor()
    valor_aluguel = aluguel.valor_nominal - aluguel.valor_nominal * 0.05    
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_aluguel, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_aluguel

#Testes do dia 11 ao dia 15
def test_dia_11_BGDF():
    aluguel = Aluguel(VALOR_NOMINAL, 11)
    valor = aluguel.calcula_valor()    
    sys.stderr.write("Esperado {} recebido {}".format(
        aluguel.valor_nominal, valor['valor_calculado']))
    assert valor['valor_calculado'] == aluguel.valor_nominal
    
def test_dia_12_BGDF():
    aluguel = Aluguel(VALOR_NOMINAL, 12)
    valor = aluguel.calcula_valor()    
    sys.stderr.write("Esperado {} recebido {}".format(
        aluguel.valor_nominal, valor['valor_calculado']))
    assert valor['valor_calculado'] == aluguel.valor_nominal

def test_dia_13_BGDF():
    aluguel = Aluguel(VALOR_NOMINAL, 13)
    valor = aluguel.calcula_valor()    
    sys.stderr.write("Esperado {} recebido {}".format(
        aluguel.valor_nominal, valor['valor_calculado']))
    assert valor['valor_calculado'] == aluguel.valor_nominal

def test_dia_14_BGDF():
    aluguel = Aluguel(VALOR_NOMINAL, 14)
    valor = aluguel.calcula_valor()    
    sys.stderr.write("Esperado {} recebido {}".format(
        aluguel.valor_nominal, valor['valor_calculado']))
    assert valor['valor_calculado'] == aluguel.valor_nominal

def test_dia_15_BGDF():    
    aluguel = Aluguel(VALOR_NOMINAL, 15)
    valor = aluguel.calcula_valor()    
    sys.stderr.write("Esperado {} recebido {}".format(
        aluguel.valor_nominal, valor['valor_calculado']))
    assert valor['valor_calculado'] == aluguel.valor_nominal

#Testes de dias após dia 15 (16, 20 e 30)
def test_dia_16_BGDF():
    DIA = 16
    aluguel = Aluguel(VALOR_NOMINAL, DIA)
    valor = aluguel.calcula_valor()
    multa = aluguel.valor_nominal * 0.02
    dias_atraso = DIA - 15 
    multa_p_dia = aluguel.valor_nominal * 0.001 * dias_atraso
    valor_multas = aluguel.valor_nominal + multa + multa_p_dia
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_multas, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_multas
    
def test_dia_20_BGDF():
    DIA = 20
    aluguel = Aluguel(VALOR_NOMINAL, DIA)
    valor = aluguel.calcula_valor()
    multa = aluguel.valor_nominal * 0.02
    dias_atraso = DIA - 15 
    multa_p_dia = aluguel.valor_nominal * 0.001 * dias_atraso
    valor_multas = aluguel.valor_nominal + multa + multa_p_dia
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_multas, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_multas

def test_dia_30_BGDF():
    DIA = 30
    aluguel = Aluguel(VALOR_NOMINAL, DIA)
    valor = aluguel.calcula_valor()
    multa = aluguel.valor_nominal * 0.02
    dias_atraso = DIA - 15 
    multa_p_dia = aluguel.valor_nominal * 0.001 * dias_atraso
    valor_multas = aluguel.valor_nominal + multa + multa_p_dia
    sys.stderr.write("Esperado {} recebido {}".format(
        valor_multas, valor['valor_calculado']))
    assert valor['valor_calculado'] == valor_multas
    
