"""Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois
   módulos internos chamados moeda e dado. Transfira todas as funções
   utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha
   tudo funcionando."""

from utilidadesCeV.moeda import resumo

while True:
    try: p = float(input("Digite um valor: R$")); break
    except ValueError: print('\033[1:31mINVÁLIDO!\033[m Tente novamente.')
resumo(p, 10, 13)
