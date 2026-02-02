"""Exercício Python 115 (3 partes):
        a) Vamos criar um menu em Python, usando modularização.
        b) Vamos ver como fazer acesso a arquivos usando o Python.
        c) Vamos finalizar o projeto de acesso a arquivos em Python."""

from def115 import *

exist_cadastros()
while True:
    i = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if i == 1:
        list_pessoas()
    elif i == 2:
        cadastrar_pessoa()
    elif i == 3:
        sair()
        break
