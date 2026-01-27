"""Exercício Python 110: Adicione ao módulo moeda.py criado nos desafios
  anteriores, uma função chamada resumo(), que mostre na tela algumas
  informações geradas pelas funções que já temos no módulo criado até aqui."""

from moeda import *

while True:
    try: p = float(input("Digite um valor: R$")); break
    except ValueError: print('\033[1:31mINVÁLIDO!\033[m Tente novamente.')
resumo(p, 10, 13)
