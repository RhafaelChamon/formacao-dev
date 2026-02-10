"""Exercício Python 109: Modifique as funções que form criadas no desafio 107
   para que elas aceitem um parâmetro a mais, informando se o valor retornado
   por elas vai ser ou não formatado pela função moeda(), desenvolvida no
   desafio 108."""

from moeda import *

while True:
    try: p = float(input("Digite um valor: R$")); break
    except ValueError: print('\033[1:31mINVÁLIDO!\033[m Tente novamente.')
print(f'Aumentando 10% de {moeda(p)}, temos {aumentar(p, 10, True)}')
print(f'Diminuindo 13% de {moeda(p)}, temos {diminuir(p, 13, True)}')
print(f'O dobro de {moeda(p)} é {dobro(p, True)}')
print(f'A metade de {moeda(p)} é {metade(p, True)}')
